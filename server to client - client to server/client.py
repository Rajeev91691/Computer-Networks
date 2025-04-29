import socket

# Create a socket object for the client
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at IP (192.168.56.1) and port (8080)
c.connect(('localhost', 12348))

# Receive a message from the server
server_message = c.recv(1024).decode()  # Decode the received bytes to a string
print("Server says:", server_message)

# Send a message to the server
c.send(bytes("Hi Server! This is the client.", 'utf-8'))

# Close the connection with the server
c.close()
