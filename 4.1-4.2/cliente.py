import socket

# IP = input("IP: ")
IP = "localhost"
# puerto = int(input("Puerto: "))
puerto = 5007
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
data = s.recv(1024).decode()
print ("Data recieved: ", data)
if(data == "OK"):
    s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("hello".encode(), (IP, puerto))





# sock = socket.socket(socket.AF_INET, # Internet
#                       socket.SOCK_DGRAM) # UDP
# sock.sendto(MESSAGE, (IP, puerto))
