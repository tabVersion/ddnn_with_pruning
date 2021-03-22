# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: edge_internal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='edge_internal.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x65\x64ge_internal.proto\"9\n\x16\x43lassifyResultsRequest\x12\x10\n\x08track_id\x18\x01 \x01(\x05\x12\r\n\x05image\x18\x02 \x03(\x05\"\'\n\x14\x43lassifyResultsReply\x12\x0f\n\x07results\x18\x01 \x03(\x01\x32P\n\tCollector\x12\x43\n\x0f\x43lassifyResults\x12\x17.ClassifyResultsRequest\x1a\x15.ClassifyResultsReply\"\x00\x62\x06proto3'
)




_CLASSIFYRESULTSREQUEST = _descriptor.Descriptor(
  name='ClassifyResultsRequest',
  full_name='ClassifyResultsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='track_id', full_name='ClassifyResultsRequest.track_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='ClassifyResultsRequest.image', index=1,
      number=2, type=5, cpp_type=1, label=3,
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
  serialized_start=23,
  serialized_end=80,
)


_CLASSIFYRESULTSREPLY = _descriptor.Descriptor(
  name='ClassifyResultsReply',
  full_name='ClassifyResultsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='ClassifyResultsReply.results', index=0,
      number=1, type=1, cpp_type=5, label=3,
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
  serialized_start=82,
  serialized_end=121,
)

DESCRIPTOR.message_types_by_name['ClassifyResultsRequest'] = _CLASSIFYRESULTSREQUEST
DESCRIPTOR.message_types_by_name['ClassifyResultsReply'] = _CLASSIFYRESULTSREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassifyResultsRequest = _reflection.GeneratedProtocolMessageType('ClassifyResultsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFYRESULTSREQUEST,
  '__module__' : 'edge_internal_pb2'
  # @@protoc_insertion_point(class_scope:ClassifyResultsRequest)
  })
_sym_db.RegisterMessage(ClassifyResultsRequest)

ClassifyResultsReply = _reflection.GeneratedProtocolMessageType('ClassifyResultsReply', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFYRESULTSREPLY,
  '__module__' : 'edge_internal_pb2'
  # @@protoc_insertion_point(class_scope:ClassifyResultsReply)
  })
_sym_db.RegisterMessage(ClassifyResultsReply)



_COLLECTOR = _descriptor.ServiceDescriptor(
  name='Collector',
  full_name='Collector',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=123,
  serialized_end=203,
  methods=[
  _descriptor.MethodDescriptor(
    name='ClassifyResults',
    full_name='Collector.ClassifyResults',
    index=0,
    containing_service=None,
    input_type=_CLASSIFYRESULTSREQUEST,
    output_type=_CLASSIFYRESULTSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COLLECTOR)

DESCRIPTOR.services_by_name['Collector'] = _COLLECTOR

# @@protoc_insertion_point(module_scope)
