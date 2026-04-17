import socket

SERVER_IP = '10.2.1.213'
SERVER_PORT = 12345
BUFFER_SIZE = 4096

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)

print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

connection_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

received_data = b''
chunk = connection_socket.recv(BUFFER_SIZE)
received_data += chunk

long_string = received_data.decode('utf-8')
print(f"Received {len(long_string)} characters")

response_string = f"Server received {len(long_string)} characters. First 100: {long_string[:100]}"
connection_socket.sendall(response_string.encode('utf-8'))
print(f"Sent response: {response_string[:100]}...")

connection_socket.close()
server_socket.close()