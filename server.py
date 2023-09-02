
import socket

# Define the server's IP address and port
host = '0.0.0.0'  # Bind to all available network interfaces
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ipv4 & TCP

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections (maximum 5 clients in the queue)
server_socket.listen(5)
print(f"Server listening on {host}:{port}")

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break  # If the client closes the connection, exit the loop

    print(f"Received data from client: {data}")

    # Echo the received data back to the client
    client_socket.send(data.encode('utf-8'))

    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()

