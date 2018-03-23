import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = 'localhost'                           

port = 12348

s.connect((host, port))                               

f = open("incoming.txt","wb")

l = s.recv(1024)
while(l):
    print("Recieving...")
    f.write(l)
    l = s.recv(1024)



f.close()
print("done recieving...")
           
s.shutdown(2)
s.close()
print("closed ports")
sys.exit()
