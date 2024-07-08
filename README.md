# DeepSpeakerService
A microservice server for an end-to-end speaker embedding model, 
[DeepSpeaker](https://github.com/philipperemy/deep-speaker).

## Model

The weight file used in this server is an official weight published in April 25th, 2020:
[Google Drive](https://drive.google.com/file/d/1F9NvdrarWZNktdX9KlRYWWHDwRkip_aP)

## Usage

Use `GetEmbedding` method of `DeepSpeakerService` service to streaming byte chunks of WAV audio file,
then the server will return the embedding of the speaker in the audio file.
There is a maximum size of gRPC content, so do not transmit too many bytes in one chunk.

**Attention**, the sample rate of the WAV audio file should be 16kHz, 
as this sample rate is configured in the server code.

The server use [librosa](https://librosa.org/doc/latest/index.html) as the backend to parsing audio file,
so any format which is supported by librosa is acceptable.

