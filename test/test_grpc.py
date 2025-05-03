# test/test_grpc.py

import grpc
import protos.story2audio_pb2 as pb2
import protos.story2audio_pb2_grpc as pb2_grpc

def test_generate_audio():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.Story2AudioServiceStub(channel)
    response = stub.GenerateAudio(pb2.TextRequest(text="Test audio generation"))
    assert response.status == "success"
    print("Test passed. Audio path:", response.audio_path)

if __name__ == '__main__':
    test_generate_audio()
