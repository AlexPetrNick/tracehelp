# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(626, 562)
        Form.setStyleSheet("background-color:#2b2b2b;")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setStyleSheet("background-color: #006934")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 100, 591, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 120, 281, 281))
        self.textEdit.setStyleSheet("color: white;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_4.setGeometry(QtCore.QRect(300, 120, 271, 281))
        self.textEdit_4.setStyleSheet("color: white;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_5.setGeometry(QtCore.QRect(10, 10, 561, 81))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(140, 100, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(420, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 10, 511, 351))
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 10, 511, 351))
        self.textEdit_3.setObjectName("textEdit_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(440, 10, 161, 91))
        self.frame.setStyleSheet("QWidget {\n"
"    background-color: gray;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(20, 50, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(90, 50, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 10, 281, 20))
        self.lineEdit.setStyleSheet("text-align: center;\n"
"border-color:2b2b2b;\n"
"background-color: gray;")
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 40, 141, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 70, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(180, 40, 121, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 70, 131, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 50, 111, 31))
        self.pushButton_3.setStyleSheet("background-color: gray;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.label_2.setText(_translate("Form", "SSCC"))
        self.label_3.setText(_translate("Form", "SGTIN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Страница"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.checkBox.setText(_translate("Form", "SGTIN"))
        self.checkBox_2.setText(_translate("Form", "SSCC"))
        self.checkBox_3.setText(_translate("Form", "Добавить шапку"))
        self.checkBox_4.setText(_translate("Form", "Добавить тело"))
        self.pushButton_3.setText(_translate("Form", " К документу"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

