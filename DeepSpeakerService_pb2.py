# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DeepSpeakerService.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x44\x65\x65pSpeakerService.proto\")\n\x10\x45mbeddingRequest\x12\x15\n\rWavAudioChunk\x18\x01 \x01(\x0c\"&\n\x11\x45mbeddingResponse\x12\x11\n\tEmbedding\x18\x01 \x03(\x02\x32M\n\x12\x44\x65\x65pSpeakerService\x12\x37\n\x0cGetEmbedding\x12\x11.EmbeddingRequest\x1a\x12.EmbeddingResponse(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'DeepSpeakerService_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMBEDDINGREQUEST']._serialized_start=28
  _globals['_EMBEDDINGREQUEST']._serialized_end=69
  _globals['_EMBEDDINGRESPONSE']._serialized_start=71
  _globals['_EMBEDDINGRESPONSE']._serialized_end=109
  _globals['_DEEPSPEAKERSERVICE']._serialized_start=111
  _globals['_DEEPSPEAKERSERVICE']._serialized_end=188
# @@protoc_insertion_point(module_scope)
