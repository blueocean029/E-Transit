import sys
import os
import socket
import threading
import time
from cryption import encrypt_file
from PyQt4 import QtCore, QtGui
import pdb

HOST="192.168.43.137"
PORT=9998
key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(335, 180)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 140, 91, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 140, 91, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 0, 321, 131))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.socket1=None
        self.conn=None
        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.textBrowser.setStyleSheet("background-image: url(t.gif);")
        self.pushButton.setStyleSheet("border: solid;border-radius:8px; border-color:#000000; color: #CCCCCC; height:50px; width:150px; font-size:11px; background-image: url(bl.jpg);")
        self.pushButton_2.setStyleSheet("border: solid;border-radius:8px; border-color:#000000; color: #CCCCCC; height:50px; width:150px; font-size:11px; background-image: url(bl.jpg);")


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Start Server", None))
        self.pushButton_2.setText(_translate("Form", "Close server", None))
        self.textBrowser.setText("Start Server")
        self.pushButton.clicked.connect(self.start_server)
        self.pushButton_2.clicked.connect(self.close1)
    def close2(self):
        if self.socket1!=None or self.conn!=None:
            self.conn.close()
            self.socket1.close()
            print "server closed"
        self.close()
    def close1(self):
        self.emit(QtCore.SIGNAL("exit"))
    def start_server(self):
        self.socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.socket1.bind((HOST, PORT))
        self.socket1.listen(5)
        self.connect(self, QtCore.SIGNAL("start_conn"),self.run)
        self.connect(self, QtCore.SIGNAL("send"),self.send)
        self.connect(self, QtCore.SIGNAL("exit"),self.close2)
        #self.create_thread()
        thread=threading.Thread(target=self.run, args=())
        thread.daemon=True
        thread.start()
    def create_thread(self):
        self.emit(QtCore.SIGNAL("start_conn"))
    def run(self):
        print "Server Started"
        QtCore.QCoreApplication.processEvents()
        while 1:
            QtCore.QCoreApplication.processEvents()
            self.conn, self.addr = self.socket1.accept()
            print "Client with ip",self.addr,"connected"
            filenames = next(os.walk("/home/prashu/Downloads"))[2]
            #self.conn.send (str(len(filenames)))
            file1=','.join(filenames)
            self.conn.send(file1)
            self.emit(QtCore.SIGNAL("send"))
            '''fname=self.conn.recv(1024)
            while not fname:
                #pass
                fname=self.conn.recv(1024)
            print "asking for : "+fname
            if os.path.isfile(fname):
                temp = open(fname,'rb')
                self.conn.send(temp.read())
                self.textBrowser.setPlainText("succesfully Sent File")
                temp.close()'''
                
            #new_socket.close()
            #self.conn.close()
            
    def send(self):
        fname=self.conn.recv(1024)
        while not fname:
            fname=self.conn.recv(1024)
            QtGui.QApplication.processEvents()
        print "asking for : " + fname
        # encrypt_file(fname,key)
        # pdb.set_trace()
        if os.path.isfile('/home/prashu/Downloads/' +fname):
            print 'here'
            temp = open('/home/prashu/Downloads/' +fname,'rb')
            var=temp.read(1024)    
            print 'sending '+  str(var)            
            self.conn.send(str(var))
            # self.conn.send("nnnnn")
            temp.close()
            if self.conn.recv(1024)=='1':
                print "client requesting again for a new file"
                #time.sleep(3)
                self.send()
            else:
                print "succesfully sent all requested files"
                #self.textBrowser.setPlainText("succesfully Sent File")
             

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    

