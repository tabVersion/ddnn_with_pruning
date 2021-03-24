import logging
import argparse
from concurrent import futures
from threading import Lock
import grpc

from protos import edge_cloud_pb2
from protos import edge_cloud_pb2_grpc

edge_addr = dict()


class NetworkSplitService(edge_cloud_pb2_grpc.NetworkSplit):

    def fetch_feature_map(self, idx, store, address='localhost:50050'):
        channel = grpc.insecure_channel(address)
        request = edge_cloud_pb2_grpc.EdgeStorageStub(channel)
        resp = request.FetchFeatureMap(
            edge_cloud_pb2.FetchFeatureMapRequest(track_id=idx)
        )
        if not resp.success:
            return
        # self.mutex.acquire()
        store[idx] = list(resp.features)
        # self.mutex.release()
        logging.info(f"[fetch_feature_map] fetch features: {list(resp.features)} index: {idx}")

    def CloudCompute(self, request, context):
        features = [None] * 4
        for _, addr in edge_addr.items():
            self.fetch_feature_map(request.track_id, features, address=addr)
        logging.info(f"[CloudCompute] get request for id: {request.track_id}")
        return edge_cloud_pb2.CloudComputeReply(label=0)


class EdgeRegisterService(edge_cloud_pb2_grpc.EdgeRegister):
    def __init__(self):
        super(EdgeRegisterService, self).__init__()
        self.register_mutex = Lock()

    def Register(self, request, context):
        self.register_mutex.acquire()
        idx = len(edge_addr)
        edge_addr[idx] = request.addr
        logging.info(f"[Register] device: {idx}, addr: {request.addr}")
        self.register_mutex.release()
        return edge_cloud_pb2.RegisterReply(device_index=idx)

    def DeviceQuery(self, request, context):
        return edge_cloud_pb2.DeviceQueryReply(device_addr=edge_addr)


def start_server(port=50000, standalone=False):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    edge_cloud_pb2_grpc.add_NetworkSplitServicer_to_server(NetworkSplitService(),
                                                           server)
    edge_cloud_pb2_grpc.add_EdgeRegisterServicer_to_server(EdgeRegisterService(),
                                                           server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info(f"[start_server] start cloud server at port {port}")
    if standalone:
        server.wait_for_termination()
    return server


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='storage service for edge server')
    parser.add_argument('port', type=int, default=50000, nargs='?', help='open service at which port')
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)
    start_server(args.port, True)
