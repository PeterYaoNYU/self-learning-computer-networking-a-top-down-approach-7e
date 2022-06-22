from socket import *
severPort=12000
sever_socket=socket(AF_INET, SOCK_DGRAM)
sever_socket.bind(('', severPort))
print('the sever is now ready to receive')
while True:
    msg, client_address=sever_socket.recvfrom(2048)
    modified_msg=msg.decode().upper()
    print(client_address)
    sever_socket.sendto(modified_msg.encode(), client_address)