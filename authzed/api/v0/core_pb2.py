# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authzed/api/v0/core.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61uthzed/api/v0/core.proto\x12\x0e\x61uthzed.api.v0\x1a\x17validate/validate.proto\"\xa0\x01\n\rRelationTuple\x12[\n\x13object_and_relation\x18\x01 \x01(\x0b\x32!.authzed.api.v0.ObjectAndRelationB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x11objectAndRelation\x12\x32\n\x04user\x18\x02 \x01(\x0b\x32\x14.authzed.api.v0.UserB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x04user\"\x9a\x02\n\x11ObjectAndRelation\x12\x66\n\tnamespace\x18\x01 \x01(\tBH\xfa\x42\x45rC(\x80\x01\x32>^([a-z][a-z0-9_]{2,61}[a-z0-9]/)?[a-z][a-z0-9_]{2,62}[a-z0-9]$R\tnamespace\x12O\n\tobject_id\x18\x02 \x01(\tB2\xfa\x42/r-(\x80\x01\x32(^([a-zA-Z0-9_][a-zA-Z0-9/_-]{0,127})|\\*$R\x08objectId\x12L\n\x08relation\x18\x03 \x01(\tB0\xfa\x42-r+(@2\'^(\\.\\.\\.|[a-z][a-z0-9_]{2,62}[a-z0-9])$R\x08relation\"\xc9\x01\n\x11RelationReference\x12\x66\n\tnamespace\x18\x01 \x01(\tBH\xfa\x42\x45rC(\x80\x01\x32>^([a-z][a-z0-9_]{2,61}[a-z0-9]/)?[a-z][a-z0-9_]{2,62}[a-z0-9]$R\tnamespace\x12L\n\x08relation\x18\x03 \x01(\tB0\xfa\x42-r+(@2\'^(\\.\\.\\.|[a-z][a-z0-9_]{2,62}[a-z0-9])$R\x08relation\"b\n\x04User\x12G\n\x07userset\x18\x02 \x01(\x0b\x32!.authzed.api.v0.ObjectAndRelationB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\x07usersetB\x11\n\nuser_oneof\x12\x03\xf8\x42\x01\"\'\n\x06Zookie\x12\x1d\n\x05token\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02 \x01R\x05token\"\xe8\x01\n\x13RelationTupleUpdate\x12U\n\toperation\x18\x01 \x01(\x0e\x32-.authzed.api.v0.RelationTupleUpdate.OperationB\x08\xfa\x42\x05\x82\x01\x02\x10\x01R\toperation\x12=\n\x05tuple\x18\x02 \x01(\x0b\x32\x1d.authzed.api.v0.RelationTupleB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x05tuple\";\n\tOperation\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x43REATE\x10\x01\x12\t\n\x05TOUCH\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\"\xf5\x01\n\x15RelationTupleTreeNode\x12R\n\x11intermediate_node\x18\x01 \x01(\x0b\x32#.authzed.api.v0.SetOperationUsersetH\x00R\x10intermediateNode\x12<\n\tleaf_node\x18\x02 \x01(\x0b\x32\x1d.authzed.api.v0.DirectUsersetH\x00R\x08leafNode\x12=\n\x08\x65xpanded\x18\x03 \x01(\x0b\x32!.authzed.api.v0.ObjectAndRelationR\x08\x65xpandedB\x0b\n\tnode_type\"\xf0\x01\n\x13SetOperationUserset\x12K\n\toperation\x18\x01 \x01(\x0e\x32-.authzed.api.v0.SetOperationUserset.OperationR\toperation\x12\x46\n\x0b\x63hild_nodes\x18\x02 \x03(\x0b\x32%.authzed.api.v0.RelationTupleTreeNodeR\nchildNodes\"D\n\tOperation\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05UNION\x10\x01\x12\x10\n\x0cINTERSECTION\x10\x02\x12\r\n\tEXCLUSION\x10\x03\";\n\rDirectUserset\x12*\n\x05users\x18\x01 \x03(\x0b\x32\x14.authzed.api.v0.UserR\x05usersBH\n\x12\x63om.authzed.api.v0Z2github.com/authzed/authzed-go/proto/authzed/api/v0b\x06proto3')



_RELATIONTUPLE = DESCRIPTOR.message_types_by_name['RelationTuple']
_OBJECTANDRELATION = DESCRIPTOR.message_types_by_name['ObjectAndRelation']
_RELATIONREFERENCE = DESCRIPTOR.message_types_by_name['RelationReference']
_USER = DESCRIPTOR.message_types_by_name['User']
_ZOOKIE = DESCRIPTOR.message_types_by_name['Zookie']
_RELATIONTUPLEUPDATE = DESCRIPTOR.message_types_by_name['RelationTupleUpdate']
_RELATIONTUPLETREENODE = DESCRIPTOR.message_types_by_name['RelationTupleTreeNode']
_SETOPERATIONUSERSET = DESCRIPTOR.message_types_by_name['SetOperationUserset']
_DIRECTUSERSET = DESCRIPTOR.message_types_by_name['DirectUserset']
_RELATIONTUPLEUPDATE_OPERATION = _RELATIONTUPLEUPDATE.enum_types_by_name['Operation']
_SETOPERATIONUSERSET_OPERATION = _SETOPERATIONUSERSET.enum_types_by_name['Operation']
RelationTuple = _reflection.GeneratedProtocolMessageType('RelationTuple', (_message.Message,), {
  'DESCRIPTOR' : _RELATIONTUPLE,
  '__module__' : 'authzed.api.v0.core_pb2'
  # @@protoc_insertion_point(class_scope:authzed.api.v0.RelationTuple)
  })
_sym_db.RegisterMessage(RelationTuple)

ObjectAndRelation = _reflection.GeneratedProtocolMessageType('ObjectAndRelation', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTANDRELATION,
  '__module__' : 'authzed.api.v0.core_pb2'
  # @@protoc_insertion_point(class_scope:authzed.api.v0.ObjectAndRelation)
  })
_sym_db.RegisterMessage(ObjectAndRelation)

RelationReference = _reflection.GeneratedProtocolMessageType('RelationReference', (_message.Message,), {
  'DESCRIPTOR' : _RELATIONREFERENCE,
  '__module__' : 'authzed.api.v0.core_pb2'
  # @@protoc_insertion_point(class_scope:authzed.api.v0.RelationReference)
  })
_sym_db.RegisterMessage(RelationReference)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'authzed.api.v0.core_pb2'
  # @@protoc_insertion_point(class_scope:authzed.api.v0.User)
  })
_sym_db.RegisterMessage(User)

Zookie = _reflection.GeneratedProtocolMessageType('Zookie', (_message.Message,), {
  'DESCRIPTOR' : _ZOOKIE,
  '__module__' : 'authzed.api.v0.core_pb2'
  # @@protoc_insertion_point(class_scope:authzed.api.v0.Zookie)
  })
_sym_db.RegisterMessage(Zookie)

RelationTupleUpdate = _reflection.GeneratedProtocolMessageType('RelationTupleUpdate', (_message.Message,), {
  'DESCRIPTOR' : _RELATIONTUPLEUPDATE,
  '__module__' : 'authzed.api.v0.core_pb2'
  # @@protoc_insertion_point(class_scope:authzed.api.v0.RelationTupleUpdate)
  })
_sym_db.RegisterMessage(RelationTupleUpdate)

RelationTupleTreeNode = _reflection.GeneratedProtocolMessageType('RelationTupleTreeNode', (_message.Message,), {
  'DESCRIPTOR' : _RELATIONTUPLETREENODE,
  '__module__' : 'authzed.api.v0.core_pb2'
  # @@protoc_insertion_point(class_scope:authzed.api.v0.RelationTupleTreeNode)
  })
_sym_db.RegisterMessage(RelationTupleTreeNode)

SetOperationUserset = _reflection.GeneratedProtocolMessageType('SetOperationUserset', (_message.Message,), {
  'DESCRIPTOR' : _SETOPERATIONUSERSET,
  '__module__' : 'authzed.api.v0.core_pb2'
  # @@protoc_insertion_point(class_scope:authzed.api.v0.SetOperationUserset)
  })
_sym_db.RegisterMessage(SetOperationUserset)

DirectUserset = _reflection.GeneratedProtocolMessageType('DirectUserset', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTUSERSET,
  '__module__' : 'authzed.api.v0.core_pb2'
  # @@protoc_insertion_point(class_scope:authzed.api.v0.DirectUserset)
  })
_sym_db.RegisterMessage(DirectUserset)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.authzed.api.v0Z2github.com/authzed/authzed-go/proto/authzed/api/v0'
  _RELATIONTUPLE.fields_by_name['object_and_relation']._options = None
  _RELATIONTUPLE.fields_by_name['object_and_relation']._serialized_options = b'\372B\005\212\001\002\020\001'
  _RELATIONTUPLE.fields_by_name['user']._options = None
  _RELATIONTUPLE.fields_by_name['user']._serialized_options = b'\372B\005\212\001\002\020\001'
  _OBJECTANDRELATION.fields_by_name['namespace']._options = None
  _OBJECTANDRELATION.fields_by_name['namespace']._serialized_options = b'\372BErC(\200\0012>^([a-z][a-z0-9_]{2,61}[a-z0-9]/)?[a-z][a-z0-9_]{2,62}[a-z0-9]$'
  _OBJECTANDRELATION.fields_by_name['object_id']._options = None
  _OBJECTANDRELATION.fields_by_name['object_id']._serialized_options = b'\372B/r-(\200\0012(^([a-zA-Z0-9_][a-zA-Z0-9/_-]{0,127})|\\*$'
  _OBJECTANDRELATION.fields_by_name['relation']._options = None
  _OBJECTANDRELATION.fields_by_name['relation']._serialized_options = b'\372B-r+(@2\'^(\\.\\.\\.|[a-z][a-z0-9_]{2,62}[a-z0-9])$'
  _RELATIONREFERENCE.fields_by_name['namespace']._options = None
  _RELATIONREFERENCE.fields_by_name['namespace']._serialized_options = b'\372BErC(\200\0012>^([a-z][a-z0-9_]{2,61}[a-z0-9]/)?[a-z][a-z0-9_]{2,62}[a-z0-9]$'
  _RELATIONREFERENCE.fields_by_name['relation']._options = None
  _RELATIONREFERENCE.fields_by_name['relation']._serialized_options = b'\372B-r+(@2\'^(\\.\\.\\.|[a-z][a-z0-9_]{2,62}[a-z0-9])$'
  _USER.oneofs_by_name['user_oneof']._options = None
  _USER.oneofs_by_name['user_oneof']._serialized_options = b'\370B\001'
  _USER.fields_by_name['userset']._options = None
  _USER.fields_by_name['userset']._serialized_options = b'\372B\005\212\001\002\020\001'
  _ZOOKIE.fields_by_name['token']._options = None
  _ZOOKIE.fields_by_name['token']._serialized_options = b'\372B\004r\002 \001'
  _RELATIONTUPLEUPDATE.fields_by_name['operation']._options = None
  _RELATIONTUPLEUPDATE.fields_by_name['operation']._serialized_options = b'\372B\005\202\001\002\020\001'
  _RELATIONTUPLEUPDATE.fields_by_name['tuple']._options = None
  _RELATIONTUPLEUPDATE.fields_by_name['tuple']._serialized_options = b'\372B\005\212\001\002\020\001'
  _RELATIONTUPLE._serialized_start=71
  _RELATIONTUPLE._serialized_end=231
  _OBJECTANDRELATION._serialized_start=234
  _OBJECTANDRELATION._serialized_end=516
  _RELATIONREFERENCE._serialized_start=519
  _RELATIONREFERENCE._serialized_end=720
  _USER._serialized_start=722
  _USER._serialized_end=820
  _ZOOKIE._serialized_start=822
  _ZOOKIE._serialized_end=861
  _RELATIONTUPLEUPDATE._serialized_start=864
  _RELATIONTUPLEUPDATE._serialized_end=1096
  _RELATIONTUPLEUPDATE_OPERATION._serialized_start=1037
  _RELATIONTUPLEUPDATE_OPERATION._serialized_end=1096
  _RELATIONTUPLETREENODE._serialized_start=1099
  _RELATIONTUPLETREENODE._serialized_end=1344
  _SETOPERATIONUSERSET._serialized_start=1347
  _SETOPERATIONUSERSET._serialized_end=1587
  _SETOPERATIONUSERSET_OPERATION._serialized_start=1519
  _SETOPERATIONUSERSET_OPERATION._serialized_end=1587
  _DIRECTUSERSET._serialized_start=1589
  _DIRECTUSERSET._serialized_end=1648
# @@protoc_insertion_point(module_scope)
