import socket

IP = "127.0.0.1"
puerto = 5007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, puerto))
s.listen(1)
conn, addr = s.accept()
print( 'Conexion TCP activa en direccion:', addr)

numObj = conn.recv(1024).decode()
print("numObj: ", numObj)
conn.send("OK".encode())
conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP, puerto))

while True:
	data, addr = s.recvfrom(1024)
	print("received message:", data.decode())

# while 1:
#     data = conn.recv(1024)
#     if not data:
#     	break
#     print ("received data:", data.decode())
#     conn.send("OK".encode())  # echo
# conn.close()
# print( 'Conexion TCP cerrada en direccion:', addr)

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind((UDP_IP, UDP_PORT))

# while True:
#     data, addr = sock.recvfrom(1024) #buffersize = 1024
#     print( data)
