# run_server.py

import grpc
from concurrent import futures
import time
from grpc_server.server import Story2AudioService
import protos.story2audio_pb2_grpc as pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_Story2AudioServiceServicer_to_server(Story2AudioService(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server started on port 50051...")
    server.start()
    try:
        while True:
            print("hello")
            time.sleep(86400)  # 1 day
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
