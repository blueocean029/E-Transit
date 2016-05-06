# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uploadgui.ui'
#
# Created: Tue May 05 22:30:00 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import socket
ip='192.168.180.1'
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
        Form.resize(463, 143)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(180, 90, 121, 31))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(340, 90, 111, 31))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.connect(self, QtCore.SIGNAL("upload_file"),self.ini)
        self.create_thread()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.path=None
        QtCore.QObject.connect(self.toolButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        self.toolButton.setStyleSheet("border: solid;border-radius:8px; border-color:#000000; color: #CCCCCC; height:50px; width:150px; font-size:11px; background-image: url(bl.jpg);")
        self.toolButton_2.setStyleSheet("border: solid;border-radius:8px; border-color:#000000; color: #CCCCCC; height:50px; width:150px; font-size:11px; background-image: url(bl.jpg);")

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Select a File", None))
        self.label_2.setText(_translate("Form", "Uploading a Document to the Server", None))
        self.toolButton.setText(_translate("Form", "Upload a Doc", None))
        self.toolButton_2.setText(_translate("Form", "Exit", None))
        self.toolButton.clicked.connect(self.upload)
        self.toolButton_2.clicked.connect(self.exit1)
    def create_thread(self):
        self.emit(QtCore.SIGNAL("upload_file"))
    def exit1(self):
        client_socket.close()    
    def ini(self):
        global client_socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, 6667))
    def upload(self):
        self.path= QtGui.QFileDialog.getOpenFileName(self, "Open File", os.getcwd())
        print 'Uploaded'
        a=self.path.split('/')
        #print self.path[-1]
        client_socket.send(str(a[-1]))
        fo=open(self.path,'rb')
        data=fo.read(1024)
        client_socket.send(str(data))
        
        
        
def Start():
    global Form
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    return Form

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    #s=Start()
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
