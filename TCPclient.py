import socket

# Server address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_IP, SERVER_PORT))

# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Send the sentence to the server
client_socket.sendall(sentence.encode())

# Receive the reversed sentence from the server
reversed_sentence = client_socket.recv(1024).decode()

print("Reversed Sentence:", reversed_sentence)

# Close the socket
client_socket.close()
