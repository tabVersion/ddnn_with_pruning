# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: edge_cloud.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='edge_cloud.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x65\x64ge_cloud.proto\"<\n\x16StoreFeatureMapRequest\x12\x10\n\x08track_id\x18\x01 \x01(\x05\x12\x10\n\x08\x66\x65\x61tures\x18\x02 \x03(\x01\"\'\n\x14StoreFeatureMapReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"*\n\x16\x46\x65tchFeatureMapRequest\x12\x10\n\x08track_id\x18\x01 \x01(\x05\"9\n\x14\x46\x65tchFeatureMapReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x10\n\x08\x66\x65\x61tures\x18\x02 \x03(\x01\"+\n\x17\x44\x65leteFeatureMapRequest\x12\x10\n\x08track_id\x18\x01 \x01(\x05\"(\n\x15\x44\x65leteFeatureMapReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\'\n\x13\x43loudComputeRequest\x12\x10\n\x08track_id\x18\x01 \x01(\x05\"\"\n\x11\x43loudComputeReply\x12\r\n\x05label\x18\x01 \x01(\x05\x32\xdf\x01\n\x0b\x45\x64geStorage\x12\x43\n\x0fStoreFeatureMap\x12\x17.StoreFeatureMapRequest\x1a\x15.StoreFeatureMapReply\"\x00\x12\x43\n\x0f\x46\x65tchFeatureMap\x12\x17.FetchFeatureMapRequest\x1a\x15.FetchFeatureMapReply\"\x00\x12\x46\n\x10\x44\x65leteFeatureMap\x12\x18.DeleteFeatureMapRequest\x1a\x16.DeleteFeatureMapReply\"\x00\x32J\n\x0cNetworkSplit\x12:\n\x0c\x43loudCompute\x12\x14.CloudComputeRequest\x1a\x12.CloudComputeReply\"\x00\x62\x06proto3'
)




_STOREFEATUREMAPREQUEST = _descriptor.Descriptor(
  name='StoreFeatureMapRequest',
  full_name='StoreFeatureMapRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='track_id', full_name='StoreFeatureMapRequest.track_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='features', full_name='StoreFeatureMapRequest.features', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=80,
)


_STOREFEATUREMAPREPLY = _descriptor.Descriptor(
  name='StoreFeatureMapReply',
  full_name='StoreFeatureMapReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='StoreFeatureMapReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=121,
)


_FETCHFEATUREMAPREQUEST = _descriptor.Descriptor(
  name='FetchFeatureMapRequest',
  full_name='FetchFeatureMapRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='track_id', full_name='FetchFeatureMapRequest.track_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=165,
)


_FETCHFEATUREMAPREPLY = _descriptor.Descriptor(
  name='FetchFeatureMapReply',
  full_name='FetchFeatureMapReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='FetchFeatureMapReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='features', full_name='FetchFeatureMapReply.features', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=224,
)


_DELETEFEATUREMAPREQUEST = _descriptor.Descriptor(
  name='DeleteFeatureMapRequest',
  full_name='DeleteFeatureMapRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='track_id', full_name='DeleteFeatureMapRequest.track_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=269,
)


_DELETEFEATUREMAPREPLY = _descriptor.Descriptor(
  name='DeleteFeatureMapReply',
  full_name='DeleteFeatureMapReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='DeleteFeatureMapReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=271,
  serialized_end=311,
)


_CLOUDCOMPUTEREQUEST = _descriptor.Descriptor(
  name='CloudComputeRequest',
  full_name='CloudComputeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='track_id', full_name='CloudComputeRequest.track_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=352,
)


_CLOUDCOMPUTEREPLY = _descriptor.Descriptor(
  name='CloudComputeReply',
  full_name='CloudComputeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='CloudComputeReply.label', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=388,
)

DESCRIPTOR.message_types_by_name['StoreFeatureMapRequest'] = _STOREFEATUREMAPREQUEST
DESCRIPTOR.message_types_by_name['StoreFeatureMapReply'] = _STOREFEATUREMAPREPLY
DESCRIPTOR.message_types_by_name['FetchFeatureMapRequest'] = _FETCHFEATUREMAPREQUEST
DESCRIPTOR.message_types_by_name['FetchFeatureMapReply'] = _FETCHFEATUREMAPREPLY
DESCRIPTOR.message_types_by_name['DeleteFeatureMapRequest'] = _DELETEFEATUREMAPREQUEST
DESCRIPTOR.message_types_by_name['DeleteFeatureMapReply'] = _DELETEFEATUREMAPREPLY
DESCRIPTOR.message_types_by_name['CloudComputeRequest'] = _CLOUDCOMPUTEREQUEST
DESCRIPTOR.message_types_by_name['CloudComputeReply'] = _CLOUDCOMPUTEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StoreFeatureMapRequest = _reflection.GeneratedProtocolMessageType('StoreFeatureMapRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOREFEATUREMAPREQUEST,
  '__module__' : 'edge_cloud_pb2'
  # @@protoc_insertion_point(class_scope:StoreFeatureMapRequest)
  })
_sym_db.RegisterMessage(StoreFeatureMapRequest)

StoreFeatureMapReply = _reflection.GeneratedProtocolMessageType('StoreFeatureMapReply', (_message.Message,), {
  'DESCRIPTOR' : _STOREFEATUREMAPREPLY,
  '__module__' : 'edge_cloud_pb2'
  # @@protoc_insertion_point(class_scope:StoreFeatureMapReply)
  })
_sym_db.RegisterMessage(StoreFeatureMapReply)

FetchFeatureMapRequest = _reflection.GeneratedProtocolMessageType('FetchFeatureMapRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHFEATUREMAPREQUEST,
  '__module__' : 'edge_cloud_pb2'
  # @@protoc_insertion_point(class_scope:FetchFeatureMapRequest)
  })
_sym_db.RegisterMessage(FetchFeatureMapRequest)

FetchFeatureMapReply = _reflection.GeneratedProtocolMessageType('FetchFeatureMapReply', (_message.Message,), {
  'DESCRIPTOR' : _FETCHFEATUREMAPREPLY,
  '__module__' : 'edge_cloud_pb2'
  # @@protoc_insertion_point(class_scope:FetchFeatureMapReply)
  })
_sym_db.RegisterMessage(FetchFeatureMapReply)

DeleteFeatureMapRequest = _reflection.GeneratedProtocolMessageType('DeleteFeatureMapRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFEATUREMAPREQUEST,
  '__module__' : 'edge_cloud_pb2'
  # @@protoc_insertion_point(class_scope:DeleteFeatureMapRequest)
  })
_sym_db.RegisterMessage(DeleteFeatureMapRequest)

DeleteFeatureMapReply = _reflection.GeneratedProtocolMessageType('DeleteFeatureMapReply', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFEATUREMAPREPLY,
  '__module__' : 'edge_cloud_pb2'
  # @@protoc_insertion_point(class_scope:DeleteFeatureMapReply)
  })
_sym_db.RegisterMessage(DeleteFeatureMapReply)

CloudComputeRequest = _reflection.GeneratedProtocolMessageType('CloudComputeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDCOMPUTEREQUEST,
  '__module__' : 'edge_cloud_pb2'
  # @@protoc_insertion_point(class_scope:CloudComputeRequest)
  })
_sym_db.RegisterMessage(CloudComputeRequest)

CloudComputeReply = _reflection.GeneratedProtocolMessageType('CloudComputeReply', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDCOMPUTEREPLY,
  '__module__' : 'edge_cloud_pb2'
  # @@protoc_insertion_point(class_scope:CloudComputeReply)
  })
_sym_db.RegisterMessage(CloudComputeReply)



_EDGESTORAGE = _descriptor.ServiceDescriptor(
  name='EdgeStorage',
  full_name='EdgeStorage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=391,
  serialized_end=614,
  methods=[
  _descriptor.MethodDescriptor(
    name='StoreFeatureMap',
    full_name='EdgeStorage.StoreFeatureMap',
    index=0,
    containing_service=None,
    input_type=_STOREFEATUREMAPREQUEST,
    output_type=_STOREFEATUREMAPREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FetchFeatureMap',
    full_name='EdgeStorage.FetchFeatureMap',
    index=1,
    containing_service=None,
    input_type=_FETCHFEATUREMAPREQUEST,
    output_type=_FETCHFEATUREMAPREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteFeatureMap',
    full_name='EdgeStorage.DeleteFeatureMap',
    index=2,
    containing_service=None,
    input_type=_DELETEFEATUREMAPREQUEST,
    output_type=_DELETEFEATUREMAPREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EDGESTORAGE)

DESCRIPTOR.services_by_name['EdgeStorage'] = _EDGESTORAGE


_NETWORKSPLIT = _descriptor.ServiceDescriptor(
  name='NetworkSplit',
  full_name='NetworkSplit',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=616,
  serialized_end=690,
  methods=[
  _descriptor.MethodDescriptor(
    name='CloudCompute',
    full_name='NetworkSplit.CloudCompute',
    index=0,
    containing_service=None,
    input_type=_CLOUDCOMPUTEREQUEST,
    output_type=_CLOUDCOMPUTEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NETWORKSPLIT)

DESCRIPTOR.services_by_name['NetworkSplit'] = _NETWORKSPLIT

# @@protoc_insertion_point(module_scope)