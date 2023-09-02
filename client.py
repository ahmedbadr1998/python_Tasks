
import socket

# Define the server's IP address and port
server_ip = '0.0.0.0'  # Bind to all available network interfaces
server_port = 12345     # Change this to the port your server is listening on

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

# Send data to the server
message = "ya pop!"
client_socket.send(message.encode('utf-8'))

# Receive data from the server
data = client_socket.recv(1024).decode('utf-8')
print(f"Received from server: {data}")

# Close the socket
client_socket.close()


