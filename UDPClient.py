from socket import *
severName='127.0.0.1'
severPort=12000
client_socket=socket(AF_INET, SOCK_DGRAM)
message=input("input a sentence to be capitalizaed: ")
client_socket.sendto(message.encode(), (severName, severPort))
modifiedMsg, severAdd=client_socket.recvfrom(2048)
print(modifiedMsg.decode())
client_socket.close()

