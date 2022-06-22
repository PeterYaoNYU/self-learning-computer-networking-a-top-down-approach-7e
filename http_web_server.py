from socket import *
import sys

sever_socket=socket(AF_INET, SOCK_STREAM)
sever_port=12000
sever_socket.bind(('', sever_port))
sever_socket.listen(5)
print('the sever is now ready to connect')
while True:
    connection_socket, addr=sever_socket.accept()
    try:
        msg=connection_socket.recv(1024).decode()
        filename=msg.split()[1]
        f=open(filename[1:])
        output_data=f.read()
        http_response_header='HTTP/1.1 200 OK\nConncetion: close\nContent-Type: text/html\n'
        connection_socket.send(http_response_header.encode())
        for i in range(len(output_data)):
            connection_socket.send(output_data[i].encode())
        connection_socket.send('\r\n'.encode())
        
        connection_socket.close()
        
    except IOError:
        http_404_not_found='HTTP/1.1 404 Not Found'
        connection_socket.send(http_404_not_found.encode())
        
        connection_socket.close()
    print("the job is done. the sever is now exiting")
    sever_socket.close()
    
    sys.exit()
        
