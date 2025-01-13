import time
import grpc
from concurrent import futures
import greeter_streaming_pb2
import greeter_streaming_pb2_grpc

# Implementación del servicio con streaming del servidor
class GreeterServicer(greeter_streaming_pb2_grpc.GreeterServicer):
    def SayHelloStream(self, request, context):
        name = request.name
        for i in range(5):  # Enviará 5 mensajes al cliente
            message = f"Hello {name}, message {i + 1}"
            yield greeter_streaming_pb2.HelloReply(message=message)
            time.sleep(1)  # Simula un retraso de procesamiento

# Configuración del servidor
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_streaming_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor de streaming gRPC ejecutándose en el puerto 50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
