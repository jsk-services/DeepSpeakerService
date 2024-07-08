FROM tensorflow/tensorflow:latest-gpu

WORKDIR '/app'

COPY deep_speaker_server.py .
COPY DeepSpeakerService* .
COPY ResCNN_triplet_training_checkpoint_265.h5 .
COPY deep_speaker ./deep_speaker
COPY requirements.txt .

# Install dependency python pakcages.
RUN pip3 install -r requirements.txt
# Protobuf provided by Tensorflow doesn't have the builder.py .
RUN curl https://raw.githubusercontent.com/protocolbuffers/protobuf/main/python/google/protobuf/internal/builder.py > /usr/local/lib/python3.11/dist-packages/google/protobuf/internal/builder.py

# Update GPG Keys for CUDA, otherwise apt update can't work.
RUN curl https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb > ./cuda-keyring_1.0-1_all.deb && dpkg -i cuda-keyring_1.0-1_all.deb

RUN apt-get update && apt-get install libsndfile-dev -y

EXPOSE 9000

ENTRYPOINT ["python3", "deep_speaker_server.py"]