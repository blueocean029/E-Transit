import pyaudio
import socket
import sys
import thread
import time

def audio_init():
    """ Pyaudio Initialization """
    chunk = 1024
    size=1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 10240
    p = pyaudio.PyAudio()
    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,frames_per_buffer = chunk)
    return stream

def socket_init():
    """ Socket Initialization """
    # host = socket.gethostname()
    host = '192.168.180.1'
    port = 50009
    backlog = 5
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))
    s.listen(backlog)
    return s

def socket_handler(client):
    chunk= 1024
    size = 1024
    stream = audio_init()
    # Main Functionality
    while 1:
        #data = client.recv(size)
        data = stream.read(chunk)
        if data:
            # Write data to pyaudio stream
            #stream.write(data)  # Stream the recieved audio data
            client.send(data)  # Send an ACK
            client.recv(size)
            

def run():
    s = socket_init()
    while(1):
        client, address = s.accept()
        print 'Incoming connection'
        thread.start_new_thread(socket_handler, (client,))


def exit():
    client.close()
    stream.close()
    p.terminate()
def Main():
    run()
if __name__=='__main__':
    #run()
    #exit()
    Main()
