import socket
import sys

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# get local machine name
host = 'localhost'                           

port = 12348

# connection to hostname on the port.
s.connect((host, port))                               

f = open("incoming.txt","wb")

l = s.recv(1024)
while(l):
    print("Recieving...")
    f.write(l)
    l = s.recv(1024)



f.close()
print("done recieving...")

# Receive no more than 1024 bytes
                                   
s.shutdown(2)
s.close()
print("closed ports")
sys.exit()
