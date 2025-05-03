# grpc_server/server.py

from concurrent import futures
import grpc
import protos.story2audio_pb2 as pb2
import protos.story2audio_pb2_grpc as pb2_grpc
from grpc_server.handler import TTSHandler

class Story2AudioService(pb2_grpc.Story2AudioServiceServicer):
    def __init__(self):
        self.handler = TTSHandler()

    def GenerateAudio(self, request, context):
        text = request.text
        if not text.strip():
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Text cannot be empty')
            return pb2.AudioResponse(audio_content='', status='failed')

        audio_bytes = self.handler.generate_audio(text)
        return pb2.AudioResponse(audio_content=audio_bytes, status='success')
