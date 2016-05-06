#!/usr/bin/env python
import pyaudio
import socket
import subprocess
import sys
import time
import MySQLdb
from Tkinter import *

#CONFIGURE NEW IP
#Creates new window
IpConfig = Tk() # make object of TK
IpConfig.configure(background = 'white') # backgroud
IpConfig.title('LOGIN CLIENT')  # title name
IpConfig.geometry('400x300')  # box size


name = StringVar()  # store what ever u enter
password = StringVar()  # store what ever u enter

Label(IpConfig, font  = ('Helvetica',22), text = 'Username', bg = 'white').place(x=130,y=40)


#Creates box for user to type IP in.
Entry(IpConfig,textvariable=name, bg = "light blue").place(x=140,y=90) # enter ur ipaddress

Label(IpConfig, font  = ('Helvetica',22), text = 'Password', bg = 'white').place(x=130,y=120)


#Creates box for user to type IP in.
Entry(IpConfig,textvariable=password, bg = "light blue").place(x=140,y=170) # enter ur ipaddress

 #Store New Ip
def IpStore():
     #Retrieves new IP from text box and stores it in variable GetIpNew
     username = name.get()
     #print username
     userpassword = password.get()
     #print userpassword
     db=MySQLdb.connect(host='192.168.180.1',port=3306,user='root',passwd='',db='minor')
     # prepare a cursor object using cursor() method
     cursor = db.cursor()
     query=cursor.execute("""Select * from client""")    # execution of query from database 
     for j in cursor.fetchall():   # execute loop upto end data
          #print j[1],j[2]
          if j[1] == username and j[2] == userpassword:
               print ('verified')
               subprocess.call("clientgui.py", shell=True)
          else:
               print ('error')
     # close the cursor object
     cursor.close ()
     # close the connection
     sys.exit()

#Calls on function IpStore in order to store the new IP
Button(IpConfig,text = 'Login', command = IpStore).place(x=170,y=220)   # call function when button press
IpConfig.mainloop()

