import unittest
import grpc
import logging
import os
import signal
import subprocess
import time

from protos import edge_cloud_pb2_grpc
from protos import edge_cloud_pb2
import cloud_server


class TestCloudServer(unittest.TestCase):

    def test_RegisterAndCloudCompute(self):
        """
        trigger CloudCompute & Register
        ``notice``: edge server should be started after cloud server
        """
        c_server = cloud_server.start_server()
        time.sleep(1)
        edge1 = subprocess.Popen("cd ../edge && python edge_server.py &",
                                 stdout=subprocess.PIPE,
                                 shell=True,
                                 preexec_fn=os.setsid)
        edge2 = subprocess.Popen("cd ../edge && python edge_server.py 50051 &",
                                 stdout=subprocess.PIPE,
                                 shell=True,
                                 preexec_fn=os.setsid)
        time.sleep(1)
        # register
        self.assertEqual(len(cloud_server.edge_addr), 2)

        # ===========

        channel = grpc.insecure_channel('localhost:50050')
        request = edge_cloud_pb2_grpc.EdgeStorageStub(channel)
        resp = request.StoreFeatureMap(
            edge_cloud_pb2.StoreFeatureMapRequest(track_id=1,
                                                  features=[1.0, 2.0, 3.0])
        )
        self.assertEqual(resp.success, True)

        # CloudCompute
        channel = grpc.insecure_channel('localhost:50000')
        request = edge_cloud_pb2_grpc.NetworkSplitStub(channel)

        resp = request.CloudCompute(
            edge_cloud_pb2.CloudComputeRequest(track_id=1)
        )
        self.assertEqual(resp.label, 0)

        # ===========

        request = edge_cloud_pb2_grpc.EdgeRegisterStub(channel)
        resp = request.DeviceQuery(
            edge_cloud_pb2.DeviceQueryRequest()
        )
        self.assertEqual(len(resp.device_addr), 2)

        # cleaning up
        os.killpg(os.getpgid(edge1.pid), signal.SIGTERM)
        os.killpg(os.getpgid(edge2.pid), signal.SIGTERM)


if __name__ == '__main__':
    unittest.main()
    logging.basicConfig()
    logging.setLevel(logging.DEBUG)
