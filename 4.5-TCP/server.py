import socket    
import sys       
import hashlib

archivo = sys.argv[1]

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

IP = "localhost"
port = 12348
# connect to localhost
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, port))
s.listen(1) # num of conections before refusing
conn, addr = s.accept()
print( 'Conexion TCP activa en direccion:', addr)




hash = md5(archivo)
# print(hash)
print("hash: " + hash)
print("sending hash...")
conn.send((str(hash)+":START").encode())

print("hash sent...")


data = conn.recv(1024).decode()

if(data=="BEGIN"):
    print("Sending file...")




f = open(archivo,'rb')
l = f.read(1024)

while (l):
    print('Sending file...')
    conn.send(l)
    l = f.read(1024)
f.close()


print("Done Sending")

conn.shutdown(2)
conn.close()   
# s.shutdown(2)
s.close() 
print("closed ports")
# print(md5("arch.txt"))
sys.exit()


