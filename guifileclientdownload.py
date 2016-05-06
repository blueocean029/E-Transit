
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guifileclient.ui'
#
# Created: Mon May 04 14:01:19 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import socket
from cryption import decrypt_file
import sys
import time
key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
host="192.168.43.137"
port=9998
Form=None
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
        Form.resize(452, 236)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 210, 101, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        #self.textEdit = QtGui.QTextEdit(Form)
        #self.textEdit.setGeometry(QtCore.QRect(10, 169, 431, 31))
        #self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 431, 181))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        #thread1=threading.Thread(target=self.recieve, args=())
        #thread1.daemon=True
        #thread1.start()
        self.prompt=None
        self.connect(self, QtCore.SIGNAL("receive_file"),self.recieve)
        self.create_thread()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.textBrowser.setStyleSheet("font:bold;font-size:14px;font-family:Arial, Helvetica;")
        self.textBrowser.setStyleSheet("background-image: url(t.gif);")
        self.pushButton.setStyleSheet("border: solid;border-radius:8px; border-color:#000000; color: #CCCCCC; height:50px; width:150px; font-size:11px; background-image: url(bl.jpg);")

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Download Doc", None))
        self.pushButton.clicked.connect(self.download1)
    def recieve(self):
        global soc
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((host,port))
        filename=soc.recv(1024)
        f=filename.split(',')
        for i in range(len(f)):
            self.textBrowser.append(f[i]+'\n')
    def create_thread(self):
         self.emit(QtCore.SIGNAL("receive_file"))
    def download1(self):
        while 1:
            print 'client'
            #fn=''
            fn, result = QtGui.QInputDialog.getText(self, "Download Doc","Enter Filename to Download")
            #fn=self.textEdit.toPlainText()
            #time.sleep(2)
            '''while not fn:
                fn=self.textEdit.toPlainText()'''
            if fn:
                print 'sending ' + str(fn)
                soc.send(str(fn))
                fdata=soc.recv(1024)
                print 'receive == ' + fdata
                fo=open(fn+".encry",'wb')
                # while fdata!='nnnnn':
                fo.write(fdata)
                    # fdata=soc.recv(1024)
                fo.close()
                # decrypt_file(fn,key)
                self.prompt, result = QtGui.QInputDialog.getText(self, "Download Successful","Enter 1 to Download Again")    
                #self.textEdit.setText('')
                soc.send(str(self.prompt))
                if str(self.prompt)!='1':
                    break
                '''else:
                    self.textEdiipt.clear()'''
        QtCore.QCoreApplication.processEvents()                    
        
def Start():
    global Form
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    print 'efwf'
    return Form

    
def Main():
    app = QtGui.QApplication(sys.argv)
    #s=Start()
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    Main()
