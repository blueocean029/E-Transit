#!/usr/bin/env python
import pyaudio    #PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library. 
					#With PyAudio, you can easily use Python to play and record audio streams on a variety of platforms
import socket      #sockets are often used to establish a connection between machines.
import decrypt_try
import sys      #The sys module provides a no. of functions and variables that can be used to manipulate different parts of the runtime environment

print('connection started')

# Pyaudio Initialization
chunk = 1024      #buffer type
p = pyaudio.PyAudio()   # object make

stream = p.open(format = pyaudio.paInt16,    # paInt16 Portaudio Sample Formats
                channels = 1,
                rate = 10240,       # usually  10 times of chunk size
                output = True)

# Socket Initialization
host = socket.gethostbyname(socket.gethostname())    # get host ip address
port = 12346       
backlog = 5    #generally we use 5 as max     #no. of queued connection
size = 1024    # chunk size
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # address family, socket type and object make
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))      # bind socket with own host
s.listen(backlog)       # number of queue connection

client, address = s.accept()   # client is object of socket use send and receive connection, accept it.
print('Server Connected by',address)

# Main Functionality
while 1:
    data1 = client.recv(size) # receive data which comes  after encryption 
    data=decrypt_try.AESDecryption(data1)   # data return after decryption .....original data/ audio 
    #print data
   
    if data:
          ####-------- Write data to pyaudio stream-----------####
        stream.write(data)  # Stream the received audio data
        client.send('ACK')  # Send an Acknowledgement, since connection is TCP

client.close()
stream.close()
p.terminate()
