import socket

# Server IP and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind((SERVER_IP, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(5)
print("Server is listening on", SERVER_IP, "port", SERVER_PORT)

while True:
    # Wait for a connection from the client
    client_socket, client_address = server_socket.accept()
    print("Connected to client:", client_address)

    # Receive the sentence from the client
    sentence = client_socket.recv(1024).decode()

    # Reverse the order of words in the sentence
    reversed_sentence = ' '.join(sentence.split()[::-1])

    # Send the reversed sentence back to the client
    client_socket.sendall(reversed_sentence.encode())

    # Close the connection with the client
    client_socket.close()
