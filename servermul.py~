import sys
import socket
import threading
import select
import string
CLIST=[]
pin = 'ABC'

def xor(string, key):
    data = ''
    for char in string:
        for ch in key:
            char = chr(ord(char) ^ ord(ch))
        data += char
    return data
	
def broadcast (sock, message):
    global CLIST
    global server_socket
    for socket in CLIST:
        if socket != server_socket:        
        #if socket != server_socket and socket != sock:
            r=0
            m=''
            m1=''
            for i in message:
                if i=='>' and r==0:
                    r=r+1
                    i=''
                if r!=0:
                    m=m+i
                if r==0:
                    m1=m1+i
            #msg=message.split('>',1)
            print 'From : ', m1
            print 'Message recived : ',m
            print message
            print 'Broadcasting...\n'
            socket.send(message)
            #socket.send(str(usr))
            #socket.send(usr)

if __name__ == "__main__":

    CLIST=[]  # List for sockets
    users=[]
    ############## OUR TCP METHOD ################################
    print '||| TCP SERVER |||'
    host = ""

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind((host, 6667))
    server_socket.listen(10)
 
    CLIST.append(server_socket)   # Add socket

    while 1:
        # Get list of ready to be read with select
        read_sockets,write_sockets,error_sockets = select.select(CLIST,[],[])
        for sock in read_sockets:
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()   # New connection recieved 
                CLIST.append(sockfd)                    # Append the new connection
                users.append(str(sockfd.getpeername()[0]))
                print "Client [%s] connected" % sockfd.getpeername()[0]
                print "Client [%s, %s] connected" % addr
                sockfd.send(','.join(users))
                #broadcast(sockfd, "New client connected ",addr)

            else:
               # sockfd, addr = server_socket.accept()
               # CLIST.append(sockfd)
                try:
                    data = sock.recv(4096, )            # Data recieved from client
                    addr = sock.recv(4096, )
                    #print data
                    #print addr
                except:
                    #broadcast(sock, "Client (%s, %s) is offline" % addr,
                     #       addr)
                    #print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CLIST.remove(sock)
                    continue

                if data:                                # Client send data
                    if data == "q" or data == "Q":      # If client quit
                        #broadcast(sock, "Client (%s, %s) quit" % addr, addr)
                        print "Client (%s, %s) quit" % addr
                        sock.close()                    # Close socket
                        CLIST.remove(sock)              # Remove from our list
                    else:
                        #broadcast(sock, "\r" + '<' +str(sock.getpeername()[0])+'>'+data)
                        broadcast(sock,addr+'>'+data)                       
                
    server_socket.close()    
