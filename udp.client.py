# UDP Client
import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get local machine name
host = socket.gethostname()

# Set the server address and port
server_address = (host, 12345)

# Send data to server
message = b'Hello, milan!'
client_socket.sendto(message, server_address)

# Receive response from server
data, server = client_socket.recvfrom(1024)
print(f'Received response from {server}: {data.decode()}')