import grpc
import greeter_streaming_pb2
import greeter_streaming_pb2_grpc

# Cliente que recibe un flujo de mensajes del servidor
def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeter_streaming_pb2_grpc.GreeterStub(channel)
        name = input("Ingrese su nombre: ")
        responses = stub.SayHelloStream(greeter_streaming_pb2.HelloRequest(name=name))

        print("Recibiendo mensajes del servidor:")
        for response in responses:
            print(response.message)

if __name__ == "__main__":
    run()
