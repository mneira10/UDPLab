import socket
import sys
import hashlib
import time

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


host = 'localhost'                           

port = 12348

s.connect((host, port))                               

print("recieving hash...")  
data = s.recv(1024).decode().split(":")
elHash = data[0]
print("hash recieved...")



if(data[1] == "START"):
    s.send("BEGIN".encode())

t = time.time()
f = open(sys.argv[1],"wb")

l = s.recv(1024)
while(l):
    print("Recieving file...")
    f.write(l)
    l = s.recv(1024)

f.close()
print("Done recieving file...")

print("Tiempo que tomo la descarga: " + str((time.time()-t)/1) + " segundos")

myHash = (md5(sys.argv[1]))



print("miHash:" + myHash)
print("elHash:" + elHash)

if(myHash==elHash):
    print("Los hash concuerdan, archivo recibido correctamente.")
else:
    print("Los hash NO concuerdan, archivo NO fue recibido correctamente.")
s.shutdown(2)
s.close()
print("closed ports")

sys.exit()


