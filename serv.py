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

test_text = "1) Сколько будет 11*11?¶а) 111¶б/ 121¶в) 22¶г) 67¶2) Что больше?¶а) -10¶б/ -1¶3) ¿Cuántas formas hay de reunir una palabra de tres letras diferentes?¶а) 3¶б) 5¶в) 9¶г/ 6¶4) Неопределенный интеграл – это функция¶а/ да¶б) нет¶5) Как от обычной теоремы синусов перейти к сферической?¶а) Заменить синусы углов на 1-sin¶б) Заменить синусы углов на их модули¶в/ Заменить длины сторон на синусы дуг¶6) Производная косинуса¶а/ -sinX¶б) sinX¶в) 1-x^2¶г)  1/(1-x^2)¶д) cosX¶е) -cosX¶7) Сколько будет 14+35?¶а) 45¶б) 59¶в/ 49¶г) 39¶8) Год рождения Колмогорова?¶а) 1900¶б/ 1903¶г) 1910¶д) 1911"

connection_socket.sendall(test_text.encode('utf-8'))
print(f"Sent response: {response_string[:100]}...")

connection_socket.close()
server_socket.close()
