import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect
port = 50000

# Bind to the port
server_socket.bind(("", port))

# Queue up to 5 requests
server_socket.listen(5)

print("Server started. Waiting for connections...")

# Accept a connection
client_socket, address = server_socket.accept()
print("Got a connection from", address)

while True:
    # Receive message from client
    message = client_socket.recv(1024).decode()
    if not message:
        break
    print("Received message:", message)

    # Send response back to client
    response = input("Server: ")
    client_socket.send(response.encode())

# Close the connection
client_socket.close()