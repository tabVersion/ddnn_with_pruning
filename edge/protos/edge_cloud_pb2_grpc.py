# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protos.edge_cloud_pb2 as edge__cloud__pb2


class EdgeStorageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StoreFeatureMap = channel.unary_unary(
                '/EdgeStorage/StoreFeatureMap',
                request_serializer=edge__cloud__pb2.StoreFeatureMapRequest.SerializeToString,
                response_deserializer=edge__cloud__pb2.StoreFeatureMapReply.FromString,
                )
        self.FetchFeatureMap = channel.unary_unary(
                '/EdgeStorage/FetchFeatureMap',
                request_serializer=edge__cloud__pb2.FetchFeatureMapRequest.SerializeToString,
                response_deserializer=edge__cloud__pb2.FetchFeatureMapReply.FromString,
                )
        self.DeleteFeatureMap = channel.unary_unary(
                '/EdgeStorage/DeleteFeatureMap',
                request_serializer=edge__cloud__pb2.DeleteFeatureMapRequest.SerializeToString,
                response_deserializer=edge__cloud__pb2.DeleteFeatureMapReply.FromString,
                )


class EdgeStorageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StoreFeatureMap(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchFeatureMap(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFeatureMap(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EdgeStorageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StoreFeatureMap': grpc.unary_unary_rpc_method_handler(
                    servicer.StoreFeatureMap,
                    request_deserializer=edge__cloud__pb2.StoreFeatureMapRequest.FromString,
                    response_serializer=edge__cloud__pb2.StoreFeatureMapReply.SerializeToString,
            ),
            'FetchFeatureMap': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchFeatureMap,
                    request_deserializer=edge__cloud__pb2.FetchFeatureMapRequest.FromString,
                    response_serializer=edge__cloud__pb2.FetchFeatureMapReply.SerializeToString,
            ),
            'DeleteFeatureMap': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFeatureMap,
                    request_deserializer=edge__cloud__pb2.DeleteFeatureMapRequest.FromString,
                    response_serializer=edge__cloud__pb2.DeleteFeatureMapReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EdgeStorage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EdgeStorage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StoreFeatureMap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EdgeStorage/StoreFeatureMap',
            edge__cloud__pb2.StoreFeatureMapRequest.SerializeToString,
            edge__cloud__pb2.StoreFeatureMapReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchFeatureMap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EdgeStorage/FetchFeatureMap',
            edge__cloud__pb2.FetchFeatureMapRequest.SerializeToString,
            edge__cloud__pb2.FetchFeatureMapReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteFeatureMap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EdgeStorage/DeleteFeatureMap',
            edge__cloud__pb2.DeleteFeatureMapRequest.SerializeToString,
            edge__cloud__pb2.DeleteFeatureMapReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class NetworkSplitStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CloudCompute = channel.unary_unary(
                '/NetworkSplit/CloudCompute',
                request_serializer=edge__cloud__pb2.CloudComputeRequest.SerializeToString,
                response_deserializer=edge__cloud__pb2.CloudComputeReply.FromString,
                )


class NetworkSplitServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CloudCompute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NetworkSplitServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CloudCompute': grpc.unary_unary_rpc_method_handler(
                    servicer.CloudCompute,
                    request_deserializer=edge__cloud__pb2.CloudComputeRequest.FromString,
                    response_serializer=edge__cloud__pb2.CloudComputeReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NetworkSplit', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NetworkSplit(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CloudCompute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkSplit/CloudCompute',
            edge__cloud__pb2.CloudComputeRequest.SerializeToString,
            edge__cloud__pb2.CloudComputeReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class EdgeRegisterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/EdgeRegister/Register',
                request_serializer=edge__cloud__pb2.RegisterRequest.SerializeToString,
                response_deserializer=edge__cloud__pb2.RegisterReply.FromString,
                )


class EdgeRegisterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EdgeRegisterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=edge__cloud__pb2.RegisterRequest.FromString,
                    response_serializer=edge__cloud__pb2.RegisterReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EdgeRegister', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EdgeRegister(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EdgeRegister/Register',
            edge__cloud__pb2.RegisterRequest.SerializeToString,
            edge__cloud__pb2.RegisterReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
