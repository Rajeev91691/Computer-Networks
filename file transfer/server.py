# server.py
import socket

# Define server IP and port
HOST = '192.168.56.1'  # Change to your local IP if needed
PORT = 55

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Accept one client at a time

print(f"Server listening on {HOST}:{PORT}")

while True:
    print("Waiting for a client connection...")
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    # Receive file request
    file_request = conn.recv(1024).decode()
    print(f"Client requested file: {file_request}")

    try:
        # Read and send file data
        with open(file_request, "r") as file:
            file_data = file.read()
        conn.sendall(file_data.encode())
        print("File sent successfully.")
    except FileNotFoundError:
        error_message = "Error: File not found"
        conn.sendall(error_message.encode())
        print("File not found error sent to client.")

    conn.close()
    print("Connection closed.")
    break