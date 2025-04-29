import socket  # Import the socket module for network communication

# Create a socket object for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# Connect the client to the server's IP and port
client_socket.connect(('192.168.56.1', 54))  
print(f"Connected to the server at {'192.168.56.1'} on port 54")

# Infinite loop to exchange messages with the server
while True:
    # Send a message to the server
    client_message = input("You: ")  # Input message from the client user
    client_socket.send(bytes(client_message, 'utf-8'))  # Send the client's message to the server
    
    # Check if the client wants to end the chat
    if client_message.lower() == "bye":
        print("You ended the chat.")
        break
    
    # Receive a message from the server
    server_message = client_socket.recv(1024).decode()  
    print("Server:", server_message)  # Display the server's message
    
    # Check if the server wants to end the chat
    if server_message.lower() == "bye":
        print("Server ended the chat.")
        break

# Close the connection
client_socket.close()
print("Connection closed.")
