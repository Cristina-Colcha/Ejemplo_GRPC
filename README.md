# Streaming Greetings Service with grpc.

This project implements a gRPC service using Python, where the server sends messages in a stream to the client. The client requests the service by providing a name and the server responds with various greetings.

## Requirements
    Python 3.6 or higher
    grpcio (for gRPC communication)
    grpcio-tools (for generating code files from the .proto file)
### Installation
    Clone this repository on your local machine:

    git clone https://github.com/Cristina-Colcha/Ejemplo_GRPC.git
    cd your-project-grpc
### Install the necessary dependencies:

     pip install grpcio grpcio-tools
    Generate the necessary Python files from the .proto file:

        python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. greeter_streaming.proto
    Project Structure

    /example-grpc
    ├── greeter_streaming.proto # gRPC service definition file.
    ├─── greeter_streaming_pb2.py # gRPC generated files.
    ├── greeter_streaming_pb2_grpc.py
    ├─── server_streaming.py # gRPC server implementation.
    ├─── client_streaming.py # Implementation of gRPC client
    └─── README.md # This file.
### Usage
Run the server
Start the server on port 50051:
    python server_streaming.py
The server will be listening for client requests.

Run the client
In another terminal, run the client:
    
    python client_streaming.py
The client will ask for your name and then display the greeting messages sent by the server one by one.

### Example of interaction
    Client:

    Enter your name: Alice
    Receiving messages from the server:
    Hello Alice, message 1
    Hello Alice, message 2
    Hello Alice, message 3
    Hello Alice, message 4
    Hello Alice, message 5
    Explanation
    The client sends a name to the server using the HelloRequest message.
    The server receives the name and generates a greeting message to the client every second.
    The client receives the messages one by one in a stream of responses and prints them.
### Technologies Used
    gRPC: High-performance communication based on HTTP/2 protocols, ideal for distributed services.
    Python: Language used to implement the server and client.
    Protocol Buffers (Proto): Definition of the message and service schema.
### Author
Cristina Colcha
