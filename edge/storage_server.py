import logging
from concurrent import futures
import grpc
import pickle
import os
import argparse
import socket

from protos import edge_cloud_pb2
from protos import edge_cloud_pb2_grpc


class EdgeStorage(edge_cloud_pb2_grpc.EdgeStorage):

    def StoreFeatureMap(self, request, context):
        track_id = request.track_id
        features = list(request.features)
        logging.info(f"[EdgeStorage.StoreFeatureMap] track_id: {track_id},"
                     f"features: {features}")
        try:
            with open(f"./track_id_{track_id}", "wb") as f:
                pickle.dump(features, f)
        except Exception as e:
            logging.warning(f"[StoreFeatureMap] err: {e}")
            return edge_cloud_pb2.StoreFeatureMapReply(success=False)
        return edge_cloud_pb2.StoreFeatureMapReply(success=True)

    def FetchFeatureMap(self, request, context):
        track_id = request.track_id
        try:
            with open(f"./track_id_{track_id}", "rb") as f:
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
        try:
            if os.path.exists(f"./track_id_{track_id}"):
                os.remove(f"./track_id_{track_id}")
        except Exception as e:
            logging.warning(f"[DeleteFeatureMap] err: {e}")
            return edge_cloud_pb2.DeleteFeatureMapReply(success=False)
        logging.info(f"[DeleteFeatureMap] delete storage for index: {track_id}")
        return edge_cloud_pb2.StoreFeatureMapReply(success=True)


def register(port):
    channel = grpc.insecure_channel('localhost:50000')
    request = edge_cloud_pb2_grpc.EdgeRegisterStub(channel)
    host = socket.gethostbyname(socket.gethostname())
    resp = request.Register(
        edge_cloud_pb2.RegisterRequest(addr=host + ':' + str(port))
    )
    return resp.device_index


def start_server(port=50050, standalone=False):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    edge_cloud_pb2_grpc.add_EdgeStorageServicer_to_server(EdgeStorage(),
                                                          server)
    register(port)
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
