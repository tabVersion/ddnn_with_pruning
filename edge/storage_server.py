import logging
from concurrent import futures
import grpc
import pickle
import os

from protos import edge_cloud_pb2
from protos import edge_cloud_pb2_grpc


class EdgeStorage(edge_cloud_pb2_grpc.EdgeStorage):

    def StoreFeatureMap(self, request, context):
        track_id = request.track_id
        features = request.features

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
            return edge_cloud_pb2.StoreFeatureMapReply(success=False)
        return edge_cloud_pb2.StoreFeatureMapReply(success=True,
                                                   features=features)

    def DeleteFeatureMap(self, request, context):
        track_id = request.track_id
        try:
            if os.path.exists(f"./track_id_{track_id}"):
                os.remove(f"./track_id_{track_id}")
        except Exception as e:
            logging.warning(f"[DeleteFeatureMap] err: {e}")
            return edge_cloud_pb2.DeleteFeatureMapReply(success=False)
        return edge_cloud_pb2.StoreFeatureMapReply(success=True)


def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    edge_cloud_pb2_grpc.add_EdgeStorageServicer_to_server(EdgeStorage(),
                                                          server)
    server.add_insecure_port('[::]:50050')
    server.start()
    server.wait_for_termination()
    return server


if __name__ == '__main__':
    logging.basicConfig()
    start_server()
