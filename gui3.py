
from PyQt4 import QtCore, QtGui
import socket
import threading
import string
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
        Form.resize(517, 339)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 391, 211))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_3 = QtGui.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(400, 50, 111, 211))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.textBrowser_2 = QtGui.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(60, 10, 341, 41))
        self.textBrowser_2.setStyleSheet(_fromUtf8("style=\"background-color:#FFDFAA\" align=\"center\""))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 260, 501, 73))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textEdit = QtGui.QTextEdit(self.layoutWidget)
        self.textEdit.setMinimumSize(QtCore.QSize(231, 0))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QtCore.QSize(101, 0))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(_fromUtf8("style=\"background-color:#FFDFAA\" align=\"center\"rgb(255, 255, 127)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(41, 0))
        self.pushButton_2.setStyleSheet(_fromUtf8("style=\"background-color:#FFDFAA\" align=\"center\"\n"
"font: italic 8pt \"MS Shell Dlg 2\"rgb(255, 255, 127);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(10, 10, 51, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(80, 40))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(400, 10, 111, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("image1.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(19, 19))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_2.setStyleSheet("background-color: #D8D8D8");
        self.pushButton.setStyleSheet("background-color:#D2D71E");
        self.pushButton_2.setStyleSheet("background-color:#D2D71E");
        self.pushButton.clicked.connect(self.send_data)
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True    # Daemonize thread
        thread.start()
        self.username=None
        self.textEdit.setStyleSheet("font:bold;font-size:18px;font-family:Arial, Helvetica;")
        self.textBrowser.setStyleSheet("color:blue;font-size:13px")
        self.textBrowser_3.setStyleSheet("color:blue;font-size:10px")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.actionCLOSE = QtGui.QAction(Form)
        self.actionCLOSE.setObjectName(_fromUtf8("actionCLOSE"))
        QtCore.QObject.connect(self.actionCLOSE, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), Form.close)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        self.textBrowser.setStyleSheet("background-image: url(t.gif);")
        self.textBrowser_3.setStyleSheet("background-image: url(t.gif);")
        #self.textEdit.setStyleSheet("background-image: url(t.gif);")

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#ffdfaa\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#aaaaff;\">          </span><span style=\" font-size:11pt; font-weight:600; font-style:italic; text-decoration: underline; color:#aaaaff;\">GROUP DISCUSSION</span></p></body></html>", None))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Georgia,Times New Roman,Times,serif\';\"><br /></p></body></html>", None))
        self.pushButton.setText(_translate("Form", "SEND", None))
        self.pushButton_2.setText(_translate("Form", "LOGOUT", None))
        self.toolButton.setText(_translate("Form", "...", None))
        self.toolButton_2.setText(_translate("Form", "GROUP MEMBERS", None))
        self.toolButton.clicked.connect(self.openInputDialog)
    def send_data(self):
        send_data=self.textEdit.toPlainText()
        #print send_data
        self.textEdit.clear()
        client_socket.send(str(send_data))
        if self.username==None:
            client_socket.send(str(client_socket.getpeername()[0]))
        else:
            client_socket.send(str(self.username))
    def run(self):
        while 1:
            try:
                recv_data = client_socket.recv(4096)
                #print recv_data
            #recv_data1 = client_socket.recv(4096)
            except:
                
                #Process terminates
                #print "Server closed connection"
                #thread.interrupt_main()     # Interrupt main wen socket closes
                break
            if not recv_data:               # If recv has no data, close conection (error)
                print "Server closed connection"
                #thread.interrupt_main()
                break
            else:
                msg=recv_data.split('>',1)
                self.textBrowser.append(str(recv_data)+'\n')
                #print "Received data: ", m
                #recv_data2 = xor(m, pin)
                print "Dectrypted data: ", msg[1]
                #print "Dectrypted data: ", msg    
    def openInputDialog(self):
        self.username, result = QtGui.QInputDialog.getText(self, "ADD","Enter Your User Name")
        #if result:
            #print "ADDED" % text
    def show_group(self,users):
        for i in range(len(users)):
            self.textBrowser_3.append(str(users[i]))
        #self.textBrowser_3.append(str(users)+'\n')
def Start():
    
    global client_socket
    global Form
    users=[]
    ip="192.168.43.137"
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, 6667))
    users1=client_socket.recv(4096)
    users1=users1.split(',')
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.show_group(users1)
    Form.show()
    
    
def Main():
    import sys
    app = QtGui.QApplication(sys.argv)
    window=Start()
    sys.exit(app.exec_())
    
    try:
        while 1:
            continue
    except:
        print "Client program quits...."
        client_socket.close()       

if __name__ == "__main__":
    Main()
