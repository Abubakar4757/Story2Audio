from concurrent import futures
import grpc
import protos.story2audio_pb2 as pb2
import protos.story2audio_pb2_grpc as pb2_grpc
from grpc_server.handler import TTSHandler

class Story2AudioService(pb2_grpc.Story2AudioServiceServicer):
    def __init__(self):
        self.handler = TTSHandler()

    def GenerateAudio(self, request, context):
        # Get the text input from the request
        text = request.text

        # Validate the text input
        if not text.strip():
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Text cannot be empty')
            return pb2.AudioResponse(audio_content=b'', status='failed', error_message="Text cannot be empty")
        
        try:
            # Generate the audio from the text using TTS handler
            audio_bytes = self.handler.generate_audio(text)

            # If no audio is generated or audio is empty, return failure
            if not audio_bytes:
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details("Audio generation failed")
                return pb2.AudioResponse(audio_content=b'', status='failed', error_message="Audio generation failed")
            
            # Return the audio content and success status
            return pb2.AudioResponse(audio_content=audio_bytes, status='success', error_message='')

        except Exception as e:
            # Catch unexpected errors and return an internal server error response
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return pb2.AudioResponse(audio_content=b'', status='failed', error_message=f"Internal server error: {str(e)}")

