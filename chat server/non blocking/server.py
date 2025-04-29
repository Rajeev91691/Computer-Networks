import socket  # Import the socket module to enable network communication

# Create a socket object for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
print("Socket created")

# Bind the socket to the specific IP address (192.168.56.1) on port 54
server_socket.bind(('192.168.56.1', 54))  
print("Socket bound to IP 192.168.56.1 and port 54")

# Start listening for incoming connections, with a maximum queue of 5
server_socket.listen(5)  
print("Waiting for connection")

# Accept a connection from a client
conn, addr = server_socket.accept()  
print("Connected with", addr)  # Print the address of the connected client

# Infinite loop to exchange messages with the client
while True:
    # Receive a message from the client
    client_message = conn.recv(1024).decode()  
    print("Client:", client_message)  # Display the client's message
    
    # Send a message back to the client
    server_message = input("You: ")  # Input message from the server user
    conn.send(bytes(server_message, 'utf-8'))  # Send the server's message to the client
    
# Close the connection
conn.close()
print("Connection closed.")
