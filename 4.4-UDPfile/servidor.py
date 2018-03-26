import socket
import time
import sys
import hashlib

# IP = input("IP del servidor: ")
# puerto = int(input("Puerto del servidor: "))
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


IP = "localhost"
puerto = 12345

archivo = "file.txt"
print("Conectando..")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Conectado.")

print("Abriendo archivo...")
f = open(archivo,'rb')
l = f.read(1024)

while (l):
	print(str(l))
	print('Sending file...')
	s.sendto(l,(IP,puerto))
	l = f.read(1024)
f.close()
print("Archivo cerrado")
s.sendto("@@@**@*@".encode(),(IP,puerto))

# s.shutdown(2)
s.close() 
print("closed ports")
# print(md5("arch.txt"))
sys.exit()
