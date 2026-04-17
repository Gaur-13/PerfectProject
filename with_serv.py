import socket

BUFFER_SIZE = 4096


def getserv(server_ip, data_string):
    server_port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    client_socket.sendall(data_string.encode('utf-8'))


    response_data = b''
    while True:
        chunk = client_socket.recv(BUFFER_SIZE)
        if not chunk:
            break
        response_data += chunk

    response_string = response_data.decode('utf-8')


    client_socket.close()
    return response_string


if __name__ == "__main__":
    SERVER_IP = '10.2.1.213'

    result = getserv(SERVER_IP, "test1")
    print(f"\nFirst 200 characters of response: {result[:200]}")