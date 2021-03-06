# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: edge_interface.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='edge_interface.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x65\x64ge_interface.proto\" \n\x0fGetImageRequest\x12\r\n\x05image\x18\x01 \x03(\x05\"\x1e\n\rGetImageReply\x12\r\n\x05label\x18\x01 \x01(\x05\x32=\n\x0bUploadImage\x12.\n\x08GetImage\x12\x10.GetImageRequest\x1a\x0e.GetImageReply\"\x00\x62\x06proto3'
)




_GETIMAGEREQUEST = _descriptor.Descriptor(
  name='GetImageRequest',
  full_name='GetImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='GetImageRequest.image', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=24,
  serialized_end=56,
)


_GETIMAGEREPLY = _descriptor.Descriptor(
  name='GetImageReply',
  full_name='GetImageReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='GetImageReply.label', index=0,
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
  serialized_start=58,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['GetImageRequest'] = _GETIMAGEREQUEST
DESCRIPTOR.message_types_by_name['GetImageReply'] = _GETIMAGEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetImageRequest = _reflection.GeneratedProtocolMessageType('GetImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETIMAGEREQUEST,
  '__module__' : 'edge_interface_pb2'
  # @@protoc_insertion_point(class_scope:GetImageRequest)
  })
_sym_db.RegisterMessage(GetImageRequest)

GetImageReply = _reflection.GeneratedProtocolMessageType('GetImageReply', (_message.Message,), {
  'DESCRIPTOR' : _GETIMAGEREPLY,
  '__module__' : 'edge_interface_pb2'
  # @@protoc_insertion_point(class_scope:GetImageReply)
  })
_sym_db.RegisterMessage(GetImageReply)



_UPLOADIMAGE = _descriptor.ServiceDescriptor(
  name='UploadImage',
  full_name='UploadImage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=90,
  serialized_end=151,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetImage',
    full_name='UploadImage.GetImage',
    index=0,
    containing_service=None,
    input_type=_GETIMAGEREQUEST,
    output_type=_GETIMAGEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_UPLOADIMAGE)

DESCRIPTOR.services_by_name['UploadImage'] = _UPLOADIMAGE

# @@protoc_insertion_point(module_scope)
