import unittest
import grpc
import logging

from protos import edge_cloud_pb2_grpc
from protos import edge_cloud_pb2


class TestCloudServer(unittest.TestCase):

    def test_CloudCompute(self):
        """
        trigger CloudCompute
        ``notice``: edge server should be started before this test
        """
        channel = grpc.insecure_channel('localhost:50000')
        request = edge_cloud_pb2_grpc.NetworkSplitStub(channel)

        resp = request.CloudCompute(
            edge_cloud_pb2.CloudComputeRequest(track_id=1)
        )
        self.assertEqual(resp.label, 0)


if __name__ == '__main__':
    unittest.main()
    logging.basicConfig()
    logging.setLevel(logging.DEBUG)
