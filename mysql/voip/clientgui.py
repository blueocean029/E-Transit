#!/usr/bin/env python
import pyaudio
import encrypt_try
import socket
import sys
import time
from Tkinter import *      # for gui library

#CONFIGURE NEW IP
#Creates new window
IpConfig = Tk()    # make object of TK
IpConfig.configure(background = 'white')  # backgroud
IpConfig.title('CLIENT')   # title name
IpConfig.geometry('300x150')  # box size


IpNew = StringVar()  # variable to store what ever u enter  

Label(IpConfig, font  = ('Helvetica',12), text = 'Please enter the IP address of the server', bg = 'white').place(x=0,y=4)


#Creates box for user to type IP in.
Entry(IpConfig,textvariable=IpNew, bg = "light blue").place(x=90,y=50)     # enter ur ip  address

 #Store New Ip
def IpStore():
     #Retrieves new IP from text box and stores it in variable GetIpNew
     #GetIpNew = IpNew.get() 
     #print ('host',GetIpNew)
     chunk = 1024
     FORMAT = pyaudio.paInt16    # port audio format
     CHANNELS = 1
     RATE = 10240
	 
     p = pyaudio.PyAudio()    # function call to get command of audio system
	 
     stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)
				
	 # Socket Initialization
     host = IpNew.get()
     port = 12346
     size = 1024
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.connect((host,port))
	 
     while 1:
        data = stream.read(chunk)      #read and put in data send it to server
        data1=encrypt_try.AESEncryption(data)
        #print data1
        s.send(data1)         
        s.recv(size)

     s.close()
     stream.close()
     p.terminate()
     #Closes window
     #IpConfig.destroy()

#Calls on function IpStore in order to store the new IP
Button(IpConfig,text = 'Call', command = IpStore).place(x=130,y=100)   # call function when button press
IpConfig.mainloop()

