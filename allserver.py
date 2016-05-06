from PyQt4 import QtCore, QtGui
import subprocess
import fileserverupload
import guifileserverdownload
import threading
import thread
import socket
import audioserver
import servermul
import videoserver
#import fileserverupload

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
        Form.resize(642, 404)
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(50, 130, 191, 41))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(370, 130, 191, 41))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_3 = QtGui.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(50, 230, 191, 41))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.toolButton_4 = QtGui.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(370, 230, 191, 41))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.toolButton_5 = QtGui.QToolButton(Form)
        self.toolButton_5.setGeometry(QtCore.QRect(210, 310, 181, 41))
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 20, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.toolButton_6 = QtGui.QToolButton(Form)
        self.toolButton_6.setGeometry(QtCore.QRect(540, 30, 91, 31))
        self.toolButton_6.setObjectName(_fromUtf8("toolButton_6"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.toolButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.toolButton.setText(_translate("Form", "Document Uploading Server", None))
        self.toolButton_2.setText(_translate("Form", "Document Downloading Server", None))
        self.toolButton_3.setText(_translate("Form", "Group Disccussion Server", None))
        self.toolButton_4.setText(_translate("Form", "Audio Broadcasting", None))
        self.toolButton_5.setText(_translate("Form", "Video Conferencing Server", None))
        self.label.setText(_translate("Form", "ALL IN ONE", None))
        self.toolButton_6.setText(_translate("Form", "EXIT", None))
        self.connect(self, QtCore.SIGNAL("doc_download"),self.doc_down)
        self.toolButton.clicked.connect(self.doc_upload)
        self.toolButton_2.clicked.connect(self.doc_download)
        self.toolButton_3.clicked.connect(self.start_discuss)
        self.toolButton_4.clicked.connect(self.start_audio)
        self.toolButton_5.clicked.connect(self.start_video)
    def doc_upload(self):
        #theproc = subprocess.Popen([sys.executable, "fileserverupload.py"])
        #theproc.communicate()
        thread.start_new_thread(self.doc_up,())
        #fileserverupload.Main()
    def doc_up(self):
        fileserverupload.Main()
        #execfile("fileserverupload.py")
    def doc_down(self):
        theproc1 = subprocess.Popen([sys.executable, "guifileserverdownload.py"])
        theproc1.communicate()
            
    def doc_download(self):
        #theproc1 = subprocess.Popen([sys.executable, "guifileserverdownload.py"])
        #theproc1.communicate()
        self.emit(QtCore.SIGNAL("doc_download"))
    def start_discuss(self):
        thread.start_new_thread(self.discuss,())
    def discuss(self):
        #theproc7 = subprocess.Popen([sys.executable, "servermul.py"])
        #theproc7.communicate()
        execfile("servermul.py")
    def start_audio(self):
        thread.start_new_thread(self.audio_broadcast,())
    def audio_broadcast(self):
        #execfile("audioserver.py")
        audioserver.Main()
    def start_video(self):
        thread.start_new_thread(self.video_broadcast,())
    def video_broadcast(self):
        #execfile("audioserver.py")
        videoserver.Main()
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

