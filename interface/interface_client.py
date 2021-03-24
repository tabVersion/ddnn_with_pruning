import grpc
import logging

from protos import edge_interface_pb2
from protos import edge_interface_pb2_grpc


def mock_interface():
    channel = grpc.insecure_channel('localhost:50050')
    request = edge_interface_pb2_grpc.UploadImageStub(channel)
    resp = request.GetImage(
        edge_interface_pb2.GetImageRequest(image=[1, 2, 3])
    )
    logging.info(f"[mock_interface] get reply: {resp.label}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    mock_interface()
