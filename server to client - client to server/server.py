import socket

# Create a socket object for the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

# Bind the server to the specific IP (192.168.56.1) and port (8080)
s.bind(('192.168.56.1', 8080))

# Listen for incoming connections (maximum 5 connections in the queue)
s.listen(5)
print("Waiting for connection")

while True:
    # Accept a connection from a client
    conn, addr = s.accept()
    print("Connected with", addr)
    
    # Send a message to the client
    conn.send(bytes("Hi, Hello! This is the server.", 'utf-8'))
    
    # Receive a message from the client
    client_message = conn.recv(1024).decode()  # Decode the received bytes to a string
    print("Client says:", client_message)
    
    # Close the connection with the client
    conn.close()
