#server side
# UDP Server
import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Bind the socket to the host and port
server_socket.bind((host, port))

print(f'Server listening on {host}:{port}')

while True:
    # Receive data from client
    data, addr = server_socket.recvfrom(1024)
    print(f'Received message from {addr}: {data.decode()}')

    # Send a response
    response = b'Hello from server!'
    server_socket.sendto(response, addr)