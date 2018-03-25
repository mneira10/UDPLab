import socket
import time

IP = input("IP del servidor: ")
puerto = int(input("Puerto del servidor: "))

numObj = int(input("Numero de objetos a enviar: "))

# TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, puerto))
s.send(str(numObj).encode())
data = s.recv(1024).decode()
s.close()
print("recibido:", data)
if(data != "OK"):
	raise Exception("debe ser ok: " + data)

# UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
contador = 1
paquetePerdidoCada = 10
while contador != numObj + 1:
	# descomente este snippet par simular 1 paquete perdido cada 10, por ejemplo
	# if contador % paquetePerdidoCada == 0:
	# 	contador += 1
	# 	continue
	obj = str(contador) + "|" + str(time.time())
	s.sendto(obj.encode(), (IP, puerto))
	print(obj, "enviado")
	contador += 1
print("listo")