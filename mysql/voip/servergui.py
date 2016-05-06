#CONFIGURE NEW IP
#Creates new window
import socket
import subprocess
from Tkinter import *



ip = socket.gethostbyname(socket.gethostname())

IpConfig = Tk()
IpConfig.configure(background = 'white')
IpConfig.title('SERVER')
IpConfig.geometry('300x150')
Label(IpConfig, font  = ('Helvetica',12), text = ' \t Server with IP Address \n\t' + ip + '\t', bg = 'white').place(x=0,y=40)

def IpStore():
     #Retrieves new IP from text box and stores it in variable GetIpNew
     subprocess.call("server.py", shell=True)
     print('connection started')
	 
	 
Button(IpConfig,text = 'start', command = IpStore).place(x=130,y=100)
IpConfig.mainloop()
