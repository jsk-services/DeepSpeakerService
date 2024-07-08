from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EmbeddingRequest(_message.Message):
    __slots__ = ("WavAudioChunk",)
    WAVAUDIOCHUNK_FIELD_NUMBER: _ClassVar[int]
    WavAudioChunk: bytes
    def __init__(self, WavAudioChunk: _Optional[bytes] = ...) -> None: ...

class EmbeddingResponse(_message.Message):
    __slots__ = ("Embedding",)
    EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    Embedding: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, Embedding: _Optional[_Iterable[float]] = ...) -> None: ...
