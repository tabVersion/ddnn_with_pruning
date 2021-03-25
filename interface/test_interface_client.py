import unittest
import logging
import os
import signal
import grpc
import subprocess
import time

from protos import edge_interface_pb2
from protos import edge_interface_pb2_grpc
from protos import edge_cloud_pb2
from protos import edge_cloud_pb2_grpc


def get_edge_address():
    channel = grpc.insecure_channel('localhost:50000')
    request = edge_cloud_pb2_grpc.EdgeRegisterStub(channel)
    resp = request.DeviceQuery(
        edge_cloud_pb2.DeviceQueryRequest()
    )
    return resp.device_addr


class TestEdgeInterface(unittest.TestCase):

    def test_interface(self):
        cloud_server = subprocess.Popen("cd ../cloud && python cloud_server.py &",
                                        stdout=subprocess.PIPE,
                                        shell=True,
                                        preexec_fn=os.setsid)
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
        edge_addrs = get_edge_address()
        channel = grpc.insecure_channel(edge_addrs[0])
        request = edge_interface_pb2_grpc.UploadImageStub(channel)
        resp = request.GetImage(
            edge_interface_pb2.GetImageRequest(image=[1, 2, 3])
        )
        self.assertEqual(resp.label, 0)
        os.killpg(os.getpgid(edge1.pid), signal.SIGTERM)
        os.killpg(os.getpgid(edge2.pid), signal.SIGTERM)
        os.killpg(os.getpgid(cloud_server.pid), signal.SIGTERM)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
