#! /usr/bin/env python3
import socket
import datetime

host_ip = '127.0.0.1'
host_port = 5000
client_ip = '127.0.0.1'
client_port = 5001
buffersize = 1024 * 1

def main():
    server = (host_ip, host_port) # Tupple
    client = (client_ip, client_port) # Tupple
    
    s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    s.bind( client )
    
    print('UDP Client Started on {}:{}'.format(client_ip, client_port))
    print('-> please write \"q\" to quit client or \"kill\" to stop server\n')
    
    message = 'Hello'
    while message != 'q':
        # Send Client data to Server
        current_time = datetime.datetime.now().time()
        print('Sending data to server: {}'.format(message))
        s.sendto(message.encode('utf-8'), server)
        
        # Recv data from Server
        recvdata, addr = s.recvfrom(buffersize)
        current_time = datetime.datetime.now().time()
        print( '{} <- Recvfrom: {}'.format(current_time, addr))
        print( 'data: {}'.format(recvdata) )
        
        message = input('->')
    s.close()
    
if __name__ == '__main__':
    main()