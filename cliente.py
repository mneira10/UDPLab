import socket

IP = raw_input("IP: ")
puerto = raw_input("Puerto: ")
numObj = raw_input("Numero de objetos a mandar: ")
print "-------------------------------"
print "IP destino: ", IP
print "Puerto destino: ", puerto
print "Numero de mensajes: ", numObj
print "-------------------------------"
print "Conectando "

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (IP, puerto))
