# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server/api/proto/v1/protoconf_mutation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from datatypes.proto.v1 import protoconf_value_pb2 as datatypes_dot_proto_dot_v1_dot_protoconf__value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='server/api/proto/v1/protoconf_mutation.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\033com.protoconf.server.api.v1'),
  serialized_pb=_b('\n,server/api/proto/v1/protoconf_mutation.proto\x12\x02v1\x1a(datatypes/proto/v1/protoconf_value.proto\"a\n\x15\x43onfigMutationRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.v1.ProtoconfValue\x12\x17\n\x0fscript_metadata\x18\x03 \x01(\t\"\x18\n\x16\x43onfigMutationResponse2a\n\x18ProtoconfMutationService\x12\x45\n\x0cMutateConfig\x12\x19.v1.ConfigMutationRequest\x1a\x1a.v1.ConfigMutationResponseB\x1d\n\x1b\x63om.protoconf.server.api.v1b\x06proto3')
  ,
  dependencies=[datatypes_dot_proto_dot_v1_dot_protoconf__value__pb2.DESCRIPTOR,])




_CONFIGMUTATIONREQUEST = _descriptor.Descriptor(
  name='ConfigMutationRequest',
  full_name='v1.ConfigMutationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='v1.ConfigMutationRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.ConfigMutationRequest.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script_metadata', full_name='v1.ConfigMutationRequest.script_metadata', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=94,
  serialized_end=191,
)


_CONFIGMUTATIONRESPONSE = _descriptor.Descriptor(
  name='ConfigMutationResponse',
  full_name='v1.ConfigMutationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=193,
  serialized_end=217,
)

_CONFIGMUTATIONREQUEST.fields_by_name['value'].message_type = datatypes_dot_proto_dot_v1_dot_protoconf__value__pb2._PROTOCONFVALUE
DESCRIPTOR.message_types_by_name['ConfigMutationRequest'] = _CONFIGMUTATIONREQUEST
DESCRIPTOR.message_types_by_name['ConfigMutationResponse'] = _CONFIGMUTATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigMutationRequest = _reflection.GeneratedProtocolMessageType('ConfigMutationRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGMUTATIONREQUEST,
  __module__ = 'server.api.proto.v1.protoconf_mutation_pb2'
  # @@protoc_insertion_point(class_scope:v1.ConfigMutationRequest)
  ))
_sym_db.RegisterMessage(ConfigMutationRequest)

ConfigMutationResponse = _reflection.GeneratedProtocolMessageType('ConfigMutationResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGMUTATIONRESPONSE,
  __module__ = 'server.api.proto.v1.protoconf_mutation_pb2'
  # @@protoc_insertion_point(class_scope:v1.ConfigMutationResponse)
  ))
_sym_db.RegisterMessage(ConfigMutationResponse)


DESCRIPTOR._options = None

_PROTOCONFMUTATIONSERVICE = _descriptor.ServiceDescriptor(
  name='ProtoconfMutationService',
  full_name='v1.ProtoconfMutationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=219,
  serialized_end=316,
  methods=[
  _descriptor.MethodDescriptor(
    name='MutateConfig',
    full_name='v1.ProtoconfMutationService.MutateConfig',
    index=0,
    containing_service=None,
    input_type=_CONFIGMUTATIONREQUEST,
    output_type=_CONFIGMUTATIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROTOCONFMUTATIONSERVICE)

DESCRIPTOR.services_by_name['ProtoconfMutationService'] = _PROTOCONFMUTATIONSERVICE

# @@protoc_insertion_point(module_scope)
