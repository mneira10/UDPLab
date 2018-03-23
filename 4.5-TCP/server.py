import socket    
import sys                                     
IP = "localhost"
port = 12348
# get local machine name
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, port))
s.listen(1) # num of conections before refusing
conn, addr = s.accept()
print( 'Conexion TCP activa en direccion:', addr)

# numObj = conn.recv(1024).decode()
# print("numObj: ", numObj)
# conn.send("OK".encode())
# conn.close()                                        

f = open("arch.txt",'rb')
print("Sending...")

l = f.read(1024)

while (l):
    print('Sending...')
    conn.send(l)
    l = f.read(1024)
f.close()
print("Done Sending")
conn.shutdown(2)
conn.close()   
s.shutdown(2)
s.close() 
print("closed ports")

sys.exit()

# while True:
#    # establish a connection
#    clientsocket,addr = serversocket.accept()      

#    print("Got a connection from %s" % str(addr))
    
#    msg = 'Thank you for connecting'+ "\r\n"
#    clientsocket.send(msg.encode('ascii'))
#    clientsocket.close()