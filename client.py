import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect
port = 50000

# Connect to the server
client_socket.connect(("localhost", port))

print("Connected to server. Type 'exit' to quit.")

while True:
    # Send message to server
    message = input("Client: ")
    if message.lower() == "exit":
        break
    client_socket.send(message.encode())

    # Receive response from server
    response = client_socket.recv(1024).decode()
    print("Server:", response)

# Close the connection
client_socket.close()