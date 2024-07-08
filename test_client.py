from datetime import datetime

import grpc
import DeepSpeakerService_pb2_grpc
from DeepSpeakerService_pb2 import *
from deep_speaker import *


def load_wav(filename):
    with open(filename, mode="rb") as file:
        while True:
            chunk = file.read(2048)
            if not chunk:
                break
            yield EmbeddingRequest(WavAudioChunk=chunk)
    return


if __name__ == '__main__':

    SERVICE_ADDRESS = ''

    with grpc.insecure_channel(SERVICE_ADDRESS) as channel:
        stub = DeepSpeakerService_pb2_grpc.DeepSpeakerServiceStub(channel)

        starting_time = datetime.now()
        response1: EmbeddingResponse = stub.GetEmbedding(load_wav("PhilippeRemy_001.wav"))
        embedding1 = response1.Embedding
        print(f"{(datetime.now() - starting_time).microseconds / 1000} ms, {embedding1}")

        starting_time = datetime.now()
        response2: EmbeddingResponse = stub.GetEmbedding(load_wav("PhilippeRemy_002.wav"))
        embedding2 = response2.Embedding
        print(f"{(datetime.now() - starting_time).microseconds / 1000} ms, {embedding2}")

        starting_time = datetime.now()
        response3: EmbeddingResponse = stub.GetEmbedding(load_wav("1255-90413-0001.flac"))
        embedding3 = response3.Embedding
        print(f"{(datetime.now() - starting_time).microseconds / 1000} ms, {embedding3}")

        same_speaker_similarity = batch_cosine_similarity([embedding1], [embedding2])
        diff_speaker_similarity = batch_cosine_similarity([embedding1], [embedding3])

        print(f"Same: {same_speaker_similarity}")
        print(f"Diff: {diff_speaker_similarity}")


