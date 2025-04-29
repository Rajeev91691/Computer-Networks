import socket  # Import the socket module to enable network communication

# Create a socket object for server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
print("Socket created")  # Print confirmation that the socket was created

# Bind the socket to a specific IP address and port
s.bind(('172.19.242.22', 8080))  

# Start listening for incoming connections, with a maximum queue of 5
s.listen(5)  
print("Waiting for connection")  # Inform that the server is ready to accept connections

# Infinite loop to keep the server running and accepting connections
while True:  
    # Accept a connection from a client
    conn, addr = s.accept()  
    print("Connected with", addr)  # Print the address of the connected client
    
    # Send a message to the client
    conn.send(bytes("Hi, Hello!", 'utf-8'))  
    
    # Close the connection with the client
    conn.close()
