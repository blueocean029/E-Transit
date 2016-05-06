# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allserver.ui'
#
# Created: Wed May 06 21:55:33 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):
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
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.toolButton.setText(_translate("Form", "Document Uploading Server", None))
        self.toolButton_2.setText(_translate("Form", "Document Downloading Server", None))
        self.toolButton_3.setText(_translate("Form", "Group Disccussion Server", None))
        self.toolButton_4.setText(_translate("Form", "Audio Broadcasting", None))
        self.toolButton_5.setText(_translate("Form", "Video Conferencing Server", None))
        self.label.setText(_translate("Form", "SERVER OF E-TRANSIT", None))
        self.toolButton_6.setText(_translate("Form", "EXIT", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

