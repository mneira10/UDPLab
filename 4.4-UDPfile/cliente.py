import socket
import _thread
import time
import os
import sys
import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

IP = "localhost"
puerto = 12345
# puerto = int(sys.argv[1])
bufferSize = 1024

print("Conectando...")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Conectado.")

print("binding..")
s.settimeout(10)
s.bind((IP, puerto))
print("binded")
print("1st packet")
# data, addr = s.recvfrom(bufferSize)
# print(data)

f = open("incoming.txt",'wb')
data = ' '.encode()
while(data.decode()!="@@@**@*@"):
	print("data")
	data, addr = s.recvfrom(bufferSize)
	if(data.decode()!="@@@**@*@"):
		f.write(data)
	print(data)
	print(addr)
	
f.close()

# s.shutdown(2)
s.close() 
print("closed ports")
# print(md5("arch.txt"))
sys.exit()