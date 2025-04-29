import socket

# Define server IP and port
HOST = '192.168.56.1'  # Change this to match the server
PORT = 55

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print(f"Connected to the server at {HOST} on port {PORT}")

# Request a file from the server
file_request = input("Enter the name of the file to request from the server: ")
client_socket.send(file_request.encode())

# Receive the file content
file_data = client_socket.recv(4096).decode()
print("\nReceived from server:")
print(file_data)

# Close the connection
client_socket.close()
print("Connection closed.")