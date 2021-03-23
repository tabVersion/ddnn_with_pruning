import logging
import argparse
from concurrent import futures
from threading import Lock
import grpc
import pickle
import os
import json

from protos import edge_cloud_pb2
from protos import edge_cloud_pb2_grpc


class NetworkSplitService(edge_cloud_pb2_grpc.NetworkSplit):

    def fetch_feature_map(self, idx, store, address='localhost'):
        channel = grpc.insecure_channel(f'{address}:50050')
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
        logging.info(f"[CloudCompute] get request for id: {request.track_id}")
        self.fetch_feature_map(request.track_id, features)
        return edge_cloud_pb2.CloudComputeReply(label=0)


def start_server(port=50000, standalone=False):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    edge_cloud_pb2_grpc.add_NetworkSplitServicer_to_server(NetworkSplitService(),
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
