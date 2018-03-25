import socket
import _thread
import time
import os
import sys

IP = "127.0.0.1"
puerto = int(sys.argv[1])
bufferSize = 1024

def atenderCliente(conn, addr):
	print("Conectado con:", addr)

	totObj = int(conn.recv(bufferSize).decode())
	conn.send("OK".encode())
	conn.close()

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.settimeout(1)
	s.bind((IP, puerto))
	ip, port = addr
	idCliente = "{}-{}".format(ip, port)
	pathName = os.path.join("archivos_clientes", idCliente + ".txt")
	perdidos = 0
	contador = totObj
	tiempoTotal = 0
	with open(pathName, "w") as f:
		while contador:
			try:
				data, addr = s.recvfrom(bufferSize)
				data = data.decode()
				print(data, "recibido")
				numObj = data.split("|")[0]
				objTime = float(data.split("|")[1])
				timeDiff = (time.time() - objTime) * 1000
				tiempoTotal += timeDiff
				f.write("{}: {:.2f} ms\n".format(numObj, timeDiff))
			except socket.timeout:
				print("paquete perdido")
				perdidos += 1
			contador -= 1
	recibidos = totObj - perdidos
	tiempoPromedio = tiempoTotal / recibidos
	tiempoPromedioFomato = "{:.2f} ms".format(tiempoPromedio)
	print("Numero de objetos recibidos:", recibidos)
	print("Numero de objetos faltantes:", perdidos)
	print("Tiempo promedio de envio:", tiempoPromedioFomato)
	print("\nRecibiendo conexiones en puerto", puerto)

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((IP, puerto))
ss.listen(1)

print("Recibiendo conexiones en puerto", puerto)
while True:
	conn, addr = ss.accept()
	_thread.start_new_thread(atenderCliente, (conn, addr))