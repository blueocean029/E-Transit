
from PyQt4 import QtCore, QtGui
#from initialui import Ui_Form
import gui3
import sys
import subprocess
import thread

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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.filename=''
        self.Form=None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(717, 436)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(-10, 0, 721, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Garamond Pro Bold"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(20, 50, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_2.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("image1.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_3 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(20, 200, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_3.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images (2).jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.toolButton_4 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(20, 100, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_4.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("download.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon2)
        self.toolButton_4.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.toolButton_5 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_5.setGeometry(QtCore.QRect(20, 150, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_5.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images (1).jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon3)
        self.toolButton_5.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.toolButton_6 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(20, 350, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_6.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("images.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon4)
        self.toolButton_6.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_6.setObjectName(_fromUtf8("toolButton_6"))
        self.toolButton_7 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_7.setGeometry(QtCore.QRect(20, 250, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_7.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("download (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon5)
        self.toolButton_7.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_7.setObjectName(_fromUtf8("toolButton_7"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(200, 40, 511, 391))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        #self.textEdit = QtGui.QTextEdit(self.centralwidget)
        #self.textEdit.setGeometry(QtCore.QRect(200, 40, 511, 391))
        #self.textEdit.setObjectName(_fromUtf8("textEdit"))
        
        self.toolButton_8 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_8.setGeometry(QtCore.QRect(20, 300, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_8.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("download.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon6)
        self.toolButton_8.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_8.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_8.setObjectName(_fromUtf8("toolButton_8"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFILE = QtGui.QMenu(self.menubar)
        self.menuFILE.setObjectName(_fromUtf8("menuFILE"))
        self.menuEDIT = QtGui.QMenu(self.menubar)
        self.menuEDIT.setObjectName(_fromUtf8("menuEDIT"))
        self.menuVIEW = QtGui.QMenu(self.menubar)
        self.menuVIEW.setObjectName(_fromUtf8("menuVIEW"))
        self.menuSETTINGS = QtGui.QMenu(self.menubar)
        self.menuSETTINGS.setObjectName(_fromUtf8("menuSETTINGS"))
        self.menuHELP = QtGui.QMenu(self.menubar)
        self.menuHELP.setObjectName(_fromUtf8("menuHELP"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW = QtGui.QAction(MainWindow)
        self.actionNEW.setObjectName(_fromUtf8("actionNEW"))
        self.actionNEW.setShortcut("Ctrl+N")
        self.actionOPEN = QtGui.QAction(MainWindow)
        self.actionOPEN.setObjectName(_fromUtf8("actionOPEN"))
        self.actionOPEN.setShortcut("Ctrl+O")
        self.actionSAVE = QtGui.QAction(MainWindow)
        self.actionSAVE.setObjectName(_fromUtf8("actionSAVE"))
        self.actionSAVE.setShortcut("Ctrl+S")
        self.actionDOWNLOAD = QtGui.QAction(MainWindow)
        self.actionDOWNLOAD.setObjectName(_fromUtf8("actionDOWNLOAD"))
        self.actionCOPY = QtGui.QAction(MainWindow)
        self.actionCOPY.setObjectName(_fromUtf8("actionCOPY"))
        self.actionCOPY.setShortcut("Ctrl+C")
        self.actionPASTE = QtGui.QAction(MainWindow)
        self.actionPASTE.setObjectName(_fromUtf8("actionPASTE"))
        self.actionPASTE.setShortcut("Ctrl+V")
        self.actionPREFERNCES = QtGui.QAction(MainWindow)
        self.actionPREFERNCES.setObjectName(_fromUtf8("actionPREFERNCES"))
        self.actionCLOSE = QtGui.QAction(MainWindow)
        self.actionCLOSE.setObjectName(_fromUtf8("actionCLOSE"))
        self.actionHELP = QtGui.QAction(MainWindow)
        self.actionHELP.setObjectName(_fromUtf8("actionHELP"))
        self.menuFILE.addAction(self.actionNEW)
        self.menuFILE.addAction(self.actionOPEN)
        self.menuFILE.addAction(self.actionSAVE)
        self.menuFILE.addAction(self.actionDOWNLOAD)
        self.menuEDIT.addAction(self.actionCOPY)
        self.menuEDIT.addAction(self.actionPASTE)
        self.menuFILE.addAction(self.actionCLOSE)
        self.menuHELP.addAction(self.actionHELP)
        self.menuSETTINGS.addAction(self.actionPREFERNCES)
        self.menubar.addAction(self.menuFILE.menuAction())
        self.menubar.addAction(self.menuEDIT.menuAction())
        self.menubar.addAction(self.menuVIEW.menuAction())
        self.menubar.addAction(self.menuSETTINGS.menuAction())
        self.menubar.addAction(self.menuHELP.menuAction())
        self.actionNEW.triggered.connect(self.new)
        self.actionOPEN.triggered.connect(self.open_file)
        self.actionCOPY.triggered.connect(self.copy)
        self.actionPASTE.triggered.connect(self.paste)
        self.actionDOWNLOAD.triggered.connect(self.download)
        self.actionSAVE.triggered.connect(self.save)
        self.actionHELP.triggered.connect(self.show_events)
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionCLOSE, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.close)
        QtCore.QObject.connect(self.toolButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

       # self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.toolButton.setText(_translate("MainWindow", "E-TRANSIT", None))
        self.toolButton_2.setText(_translate("MainWindow", "  GROUP DISCUSSION", None))
        self.toolButton_3.setText(_translate("MainWindow", "    VIDEO CALL", None))
        self.toolButton_4.setText(_translate("MainWindow", "   UPLOAD DOC", None))
        self.toolButton_5.setText(_translate("MainWindow", "   DOWNLOAD DOC", None))
        self.toolButton_6.setText(_translate("MainWindow", "    EXIT", None))
        self.toolButton_6.setShortcut(_translate("MainWindow", "Esc", None))
        self.toolButton_7.setText(_translate("MainWindow", "   AUDIO BROADCAST ", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.toolButton_8.setText(_translate("MainWindow", "     HELP", None))
        self.menuFILE.setTitle(_translate("MainWindow", "FILE", None))
        self.menuEDIT.setTitle(_translate("MainWindow", "EDIT", None))
        self.menuVIEW.setTitle(_translate("MainWindow", "VIEW", None))
        self.menuSETTINGS.setTitle(_translate("MainWindow", "SETTINGS", None))
        self.menuHELP.setTitle(_translate("MainWindow", "EVENTS", None))
        self.actionNEW.setText(_translate("MainWindow", "NEW", None))
        self.actionOPEN.setText(_translate("MainWindow", "OPEN", None))
        self.actionSAVE.setText(_translate("MainWindow", "SAVE", None))
        self.actionDOWNLOAD.setText(_translate("MainWindow", "DOWNLOAD", None))
        self.actionCOPY.setText(_translate("MainWindow", "COPY", None))
        self.actionPASTE.setText(_translate("MainWindow", "PASTE", None))
        self.actionHELP.setText(_translate("MainWindow", "UPCOMING", None))
        self.actionPREFERNCES.setText(_translate("MainWindow", "PREFERNCES", None))
        self.toolButton_8.clicked.connect(self.show_help)
        #self.toolButton_6.setShortcut(_translate("MainWindow", "Esc", None))
        self.toolButton_2.clicked.connect(self.sub_info)
        self.toolButton_4.clicked.connect(self.upload_to_server)
        self.toolButton_5.clicked.connect(self.download_to_server)
        self.toolButton_7.clicked.connect(self.audio)
        self.toolButton_2.setStyleSheet("border: solid;border-radius:8px; border-color:#000000; color: #CCCCCC; height:50px; width:150px; font-size:11px; background-image: url(bl.jpg);")
        self.toolButton_3.setStyleSheet("border: solid;border-radius:8px; border-color:#000000; color: #CCCCCC; height:50px; width:150px; font-size:11px; background-image: url(bl.jpg);")
        self.toolButton_4.setStyleSheet("border: solid;border-radius:8px; border-color:#000000; color: #CCCCCC; height:50px; width:150px; font-size:11px; background-image: url(bl.jpg);")
        self.toolButton_5.setStyleSheet("border: solid;border-radius:8px; border-color:#000000; color: #CCCCCC; height:50px; width:150px; font-size:11px; background-image: url(bl.jpg);")
        self.toolButton_6.setStyleSheet("border: solid;border-radius:8px; border-color:#000000; color: #CCCCCC; height:50px; width:150px; font-size:11px; background-image: url(bl.jpg);")
        self.toolButton_7.setStyleSheet("border: solid;border-radius:8px; border-color:#000000; color: #CCCCCC; height:50px; width:150px; font-size:11px; background-image: url(bl.jpg);")
        self.toolButton_8.setStyleSheet("border: solid;border-radius:8px; border-color:#000000; color: #CCCCCC; height:50px; width:150px; font-size:11px; background-image: url(bl.jpg);")
        self.toolButton.setStyleSheet("background-image: url(a.jpg); color:#000000;font-weight:bold ")
        self.textBrowser.setStyleSheet("background-image: url(t.gif);")
    def new(self):
        subprocess.Popen(r"C:\Windows\system32\notepad.exe")
    def upload_to_server(self):
        theproc = subprocess.Popen([sys.executable, "guifileclientupload.py"])
        theproc.communicate()
    def download_to_server(self):
        self.theproc = subprocess.Popen([sys.executable, "guifileclientdownload.py"])
        self.theproc.communicate()    
    def show_events(self):
        print "Events"
    def open_file(self):
        print "OPENING DOCUMENT"
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".","(*.txt)")
        if self.filename:
            with open(self.filename,"rt") as file:
                self.textBrowser.setText(file.read())
    def copy(self):
        print "NEW DOCUMENT"
    def audio(self):
        thread.start_new_thread(self.listen1,())
    def listen1(self):
        theproc2 = subprocess.Popen([sys.executable, "audioclient.py"])
        theproc2.communicate()
    def save(self):
        print "NEW DOCUMENT"

    def download(self):
        print "NEW DOCUMENT"

    def paste(self):
        print "NEW DOCUMENT"
    def show_help(self):
        fo=open('help.txt','rt')
        msg=fo.read(4096)
        self.textBrowser.setText(str(msg))
    def call_client(self):
        gui3.Start()
    def sub_info(self):
        #app = QtGui.QApplication(sys.argv)
        #self.Form = QtGui.QWidget()
        #register= Ui_Form()
        #register.setupUi(self.Form)
        #self.Form.show()
        #app.exec_()
        #thread.start_new_thread(self.call_client,())
        gui3.Start()
    
                
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color:#CCCCCC;border: 1px solid black;}')

    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('E-Transit')
    MainWindow.show()
    sys.exit(app.exec_())
    

