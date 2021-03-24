import unittest
import grpc
import logging

import edge_server
from protos import edge_cloud_pb2_grpc
from protos import edge_cloud_pb2


class TestStorageServer(unittest.TestCase):

    def test_all_func(self):
        """
        test all functions in edge_server.py: store, fetch, delete
        """
        server = edge_server.start_server()
        features = [1., 2., 3., 4.]

        channel = grpc.insecure_channel('localhost:50050')
        request = edge_cloud_pb2_grpc.EdgeStorageStub(channel)

        # StoreFeatureMap
        resp = request.StoreFeatureMap(
            edge_cloud_pb2.StoreFeatureMapRequest(track_id=1,
                                                  features=features)
        )
        self.assertEqual(resp.success, True)

        # FetchFeatureMap
        resp = request.FetchFeatureMap(
            edge_cloud_pb2.FetchFeatureMapRequest(track_id=1)
        )
        self.assertEqual(resp.success, True)
        self.assertEqual(resp.features, features)

        # DeleteFeatureMap
        resp = request.DeleteFeatureMap(
            edge_cloud_pb2.DeleteFeatureMapRequest(track_id=1)
        )
        self.assertEqual(resp.success, True)


if __name__ == '__main__':
    unittest.main()
    logging.basicConfig()
    logging.setLevel(logging.DEBUG)
