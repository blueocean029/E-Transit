import threading
import socket
from cryption import encrypt_file

key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'

def server(s,addr):
        while 1:
                filename=s.recv(1024)
                while not filename:
                        #print "starting"
                        filename=s.recv(1024)
                fo=open(filename,'wb')
                print '%s to be uploaded'%filename
                data=str(s.recv(1024))
                fo.write(data)
                encrypt_file(filename,key)
                print '%s created'%(filename)
                fo.close()
        s.close()                

def Main():
	print 'server started'
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	host='192.168.43.137'
	port=6667
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((host,port))
	sock.listen(7)
	while True:
                s,(h,p)=sock.accept()
                print 'client connected with ip address %s' %h
                t=threading.Thread(target=server,args=(s,h))
                t.start()
        sock.close()
if __name__=='__main__':
        Main()
