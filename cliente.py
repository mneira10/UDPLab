import socket

IP = input("IP: ")
puerto = int(input("Puerto: "))
numObj = input("Numero de objetos a mandar: ")
print ("-------------------------------")
print ("IP destino: ", IP)
print ("Puerto destino: ", puerto)
print ("Numero de mensajes: ", numObj)
print ("-------------------------------")
print ("Conectando por TCP...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, puerto))
s.send(numObj.encode())
data = s.recv(1024)
print ("Data recieved: ", data.decode())
if(data == "OK"):
    s.close()






print( "received data:", data)

# sock = socket.socket(socket.AF_INET, # Internet
#                       socket.SOCK_DGRAM) # UDP
# sock.sendto(MESSAGE, (IP, puerto))
