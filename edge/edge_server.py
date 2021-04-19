import logging
from concurrent import futures
import grpc
import pickle
import os
import argparse
import socket
from threading import Lock, Thread
import time
from computing_server import edge_compute, aggregate
from protos import edge_cloud_pb2
from protos import edge_cloud_pb2_grpc
from protos import edge_internal_pb2
from protos import edge_internal_pb2_grpc
from protos import edge_interface_pb2
from protos import edge_interface_pb2_grpc

device_num = None


class EdgeStorage(edge_cloud_pb2_grpc.EdgeStorageServicer):

    def StoreFeatureMap(self, request, context):
        track_id = request.track_id
        features = list(request.features)
        logging.info(f"[EdgeStorage.StoreFeatureMap] track_id: {track_id},"
                     f"features: {features}")
        return edge_cloud_pb2.StoreFeatureMapReply(success=True) # Test
        global device_num
        try:
            with open(f"./device_{device_num}_track_id_{track_id}", "wb") as f:
                pickle.dump(features, f)
        except Exception as e:
            logging.warning(f"[StoreFeatureMap] err: {e}")
            return edge_cloud_pb2.StoreFeatureMapReply(success=False)
        return edge_cloud_pb2.StoreFeatureMapReply(success=True)

    def FetchFeatureMap(self, request, context):
        track_id = request.track_id
        return edge_cloud_pb2.FetchFeatureMapReply(success=True,
                                                   features=[1.0] + [0.0] * 9)
        
        try:
            with open(f"./device_{device_num}_track_id_{track_id}", "rb") as f:
                features = pickle.load(f)
        except Exception as e:
            logging.warning(f"[FetchFeatureMap] err: {e}")
            return edge_cloud_pb2.FetchFeatureMapReply(success=False)
        logging.info(f"[FetchFeatureMap] request for index: {track_id}, "
                     f"features: {features}")
        return edge_cloud_pb2.FetchFeatureMapReply(success=True,
                                                   features=features)

    def DeleteFeatureMap(self, request, context):
        track_id = request.track_id
        global device_num
        try:
            if os.path.exists(f"./device_{device_num}_track_id_{track_id}"):
                os.remove(f"./device_{device_num}_track_id_{track_id}")
        except Exception as e:
            logging.warning(f"[DeleteFeatureMap] err: {e}")
            return edge_cloud_pb2.DeleteFeatureMapReply(success=False)
        logging.info(f"[DeleteFeatureMap] delete storage for index: {track_id}, "
                     f"device: {device_num}")
        return edge_cloud_pb2.StoreFeatureMapReply(success=True)


def register(port):
    channel = grpc.insecure_channel('localhost:50000')
    request = edge_cloud_pb2_grpc.EdgeRegisterStub(channel)
    host = socket.gethostbyname(socket.gethostname())
    resp = request.Register(
        edge_cloud_pb2.RegisterRequest(addr=host + ':' + str(port))
    )
    logging.info(f"[register] device number: {resp.device_index}")
    global device_num
    device_num = resp.device_index
    return resp.device_index


class CollectorService(edge_internal_pb2_grpc.CollectorServicer):

    def ClassifyResults(self, request, context):
        track_id = request.track_id
        image = request.image
        results, feature_map = edge_compute(track_id, image)

        s = int(time.time() * 1000)
        # TODO store feature map to local storage using rpc call
        try:
            with open(f"./device_{device_num}_track_id_{track_id}", "wb") as f:
                pickle.dump(feature_map, f)
            logging.info(f"[ClassifyResults] store success: "
                         f"track_id: {track_id}, features: {feature_map}")
        except Exception as e:
            logging.warning(f"[ClassifyResults] err: {e}")
        logging.info(f'[ClassifyResults] {int(time.time() * 1000) - s}ms')
        return edge_internal_pb2.ClassifyResultsReply(results=results)


def get_edge_address():
    channel = grpc.insecure_channel('localhost:50000')
    request = edge_cloud_pb2_grpc.EdgeRegisterStub(channel)
    resp = request.DeviceQuery(
        edge_cloud_pb2.DeviceQueryRequest()
    )
    return resp.device_addr


class UploadImageService(edge_interface_pb2_grpc.UploadImageServicer):
    def __init__(self):
        super(UploadImageService, self).__init__()
        self.track_id = 0
        self.accumulate_mutex = Lock()

    def GetImage(self, request, context):
        logging.info(f"[GetImage] get request: image: {request.image}")
        s = int(time.time() * 1000)
        edge_addr = get_edge_address()
        logging.info(f'[GetImage] get_edge_address: {int(time.time() * 1000) - s}ms')
        track_id = self.track_id
        with self.accumulate_mutex:
            self.track_id += 1
        s = int(time.time() * 1000)
        fu = FetchUtils(edge_addr, track_id, request.image)
        res = fu.launch()
        logging.info(f'[GetImage] fetchUtils: {int(time.time() * 1000) - s}ms')

        if aggregate(res):
            label = 0  # TODO
        else:
            channel = grpc.insecure_channel('localhost:50000')
            request = edge_cloud_pb2_grpc.NetworkSplitStub(channel)
            s = int(time.time() * 1000)
            resp = request.CloudCompute(
                edge_cloud_pb2.CloudComputeRequest(track_id=track_id)
            )
            logging.info(f'[GetImage] cloud compute: {int(time.time() * 1000) - s}ms')
            label = resp.label
        s = int(time.time() * 1000)
        fu.launch_threads(request=False)
        logging.info(f'[GetImage] delete request: {int(time.time() * 1000) - s}ms')
        return edge_interface_pb2.GetImageReply(label=label)


class FetchUtils:
    def __init__(self, edge_addr, track_id, image):
        self.collect_mutex = Lock()
        self.edge_addr = edge_addr
        self.res_collect = [None] * len(edge_addr)
        self.track_id = track_id
        self.image = image

    def launch(self):
        self.launch_threads()
        return self.res_collect

    def trigger_and_delete(self, device_id, addr, track_id, _placeholder):
        channel = grpc.insecure_channel(addr)
        request = edge_internal_pb2_grpc.CollectorStub(channel)
        _ = request.ClassifyResults(
            edge_internal_pb2.ClassifyResultsRequest(track_id=track_id)
        )

    def trigger_and_fetch(self, device_id, addr, track_id, image):
        channel = grpc.insecure_channel(addr)
        request = edge_internal_pb2_grpc.CollectorStub(channel)
        s = int(time.time() * 1000)
        resp = request.ClassifyResults(
            edge_internal_pb2.ClassifyResultsRequest(track_id=track_id,
                                                     image=image)
        )
        logging.info(f'[trigger_and_fetch] trigger: {int(time.time() * 1000 - s)}ms')
        with self.collect_mutex:
            logging.info(f"[trigger_and_fetch] device: {device_id}, "
                         f"resp: {resp.results}")
            self.res_collect[device_id] = resp.results

    def launch_threads(self, request=True):
        threads = []
        for device_id, device_addr in self.edge_addr.items():
            t = Thread(target=self.trigger_and_fetch if request else self.trigger_and_delete,
                       args=(device_id,
                             device_addr,
                             self.track_id,
                             self.image))
            t.start()
            logging.info(f'[launch_threads] thread launched: device id: {device_id}, device_addr: {device_addr}')
            threads.append(t)
        for t in threads:
            t.join()


def start_server(port=50050, standalone=False):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    edge_cloud_pb2_grpc.add_EdgeStorageServicer_to_server(EdgeStorage(),
                                                          server)
    edge_internal_pb2_grpc.add_CollectorServicer_to_server(CollectorService(),
                                                           server)
    if standalone:
        register(port)
    if device_num == 0:
        edge_interface_pb2_grpc.add_UploadImageServicer_to_server(
            UploadImageService(), server)
        logging.info(f"[start_server] interface server starts at {port}")
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info(f"[start_server] start storage server at port {port}")
    if standalone:
        server.wait_for_termination()
    return server


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='storage service for edge server')
    parser.add_argument('port', type=int, default=50050, nargs='?', help='open service at which port')
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)
    start_server(args.port, True)
