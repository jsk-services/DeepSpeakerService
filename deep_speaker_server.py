import os
from concurrent import futures
from io import BytesIO
from typing import Iterable

import grpc
import audioread
import numpy as np
import DeepSpeakerService_pb2
from deep_speaker import read_mfcc
from deep_speaker import sample_from_mfcc
from deep_speaker.conv_models import DeepSpeakerModel
from deep_speaker import batch_cosine_similarity
from deep_speaker import SAMPLE_RATE, NUM_FRAMES
import DeepSpeakerService_pb2_grpc
from DeepSpeakerService_pb2 import *

SETTINGS_MAX_THREADS = os.environ.get('SETTINGS_MAX_THREADS', 10)


class DeepSpeakerService(DeepSpeakerService_pb2_grpc.DeepSpeakerServiceServicer):
    def __init__(self):
        self._model = DeepSpeakerModel()
        self._model.m.load_weights('ResCNN_triplet_training_checkpoint_265.h5', by_name=True)

    def GetEmbedding(self, request_iterator: Iterable[DeepSpeakerService_pb2.EmbeddingRequest], context):
        buffer = BytesIO()
        for request_chunk in request_iterator:
            buffer.write(request_chunk.WavAudioChunk)
        buffer.seek(0)
        l = buffer.getbuffer().nbytes
        mfcc = sample_from_mfcc(read_mfcc(buffer, SAMPLE_RATE), NUM_FRAMES)
        embedding = self._model.m.predict(np.expand_dims(mfcc, axis=0))[0]
        return DeepSpeakerService_pb2.EmbeddingResponse(Embedding=embedding)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=SETTINGS_MAX_THREADS))
    DeepSpeakerService_pb2_grpc.add_DeepSpeakerServiceServicer_to_server(DeepSpeakerService(), server)
    server.add_insecure_port(f'[::]:9000')
    server.start()
    print(f"Server started on port 9000.")
    server.wait_for_termination()
    print(f"Server terminated.")