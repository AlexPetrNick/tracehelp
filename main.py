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
        Form.resize(683, 591)
        Form.setStyleSheet("background-color:#2b2b2b;")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setStyleSheet("background-color: #006934")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 100, 661, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 261, 361))
        self.textEdit.setStyleSheet("color: white;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_4.setGeometry(QtCore.QRect(300, 40, 331, 361))
        self.textEdit_4.setStyleSheet("color: white;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(300, 10, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_5.setGeometry(QtCore.QRect(60, 10, 101, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_6.setGeometry(QtCore.QRect(340, 10, 91, 17))
        self.checkBox_6.setObjectName("checkBox_6")
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
        self.frame.setGeometry(QtCore.QRect(160, 10, 141, 71))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: gray;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: gray;\n"
"    border: 1px solid green;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.pushButton_2.setStyleSheet("background-color: gray;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(10, 50, 51, 17))
        self.checkBox.setStyleSheet("background-color: gray;")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(80, 50, 51, 17))
        self.checkBox_2.setStyleSheet("background-color: gray;")
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 141, 41))
        self.lineEdit.setStyleSheet("text-align: center;\n"
"border-color:2b2b2b;\n"
"background-color: gray;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 90, 111, 21))
        self.pushButton_3.setStyleSheet("background-color: gray;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox_7 = QtWidgets.QCheckBox(Form)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 560, 141, 17))
        self.checkBox_7.setStyleSheet("color: white;")
        self.checkBox_7.setObjectName("checkBox_7")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(310, 10, 341, 71))
        self.frame_2.setStyleSheet("QFrame {\n"
"    background-color: gray;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: gray;\n"
"    border: 1px solid green;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 10, 141, 17))
        self.checkBox_3.setStyleSheet("background-color: gray;")
        self.checkBox_3.setObjectName("checkBox_3")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(170, 10, 141, 22))
        self.comboBox.setStyleSheet("background-color: black;\n"
"color: white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 40, 121, 17))
        self.checkBox_4.setStyleSheet("background-color: gray;")
        self.checkBox_4.setObjectName("checkBox_4")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.label_2.setText(_translate("Form", "SSCC"))
        self.label_3.setText(_translate("Form", "SGTIN"))
        self.checkBox_5.setText(_translate("Form", "Добавить"))
        self.checkBox_6.setText(_translate("Form", "Добавить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Инициализация"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Готовый файл"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Страница"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.checkBox.setText(_translate("Form", "SGTIN"))
        self.checkBox_2.setText(_translate("Form", "SSCC"))
        self.pushButton_3.setText(_translate("Form", " К документу"))
        self.checkBox_7.setText(_translate("Form", "Добавить теги к кодам"))
        self.checkBox_3.setText(_translate("Form", "Добавить шапку"))
        self.comboBox.setItemText(0, _translate("Form", "915"))
        self.comboBox.setItemText(1, _translate("Form", "913"))
        self.comboBox.setItemText(2, _translate("Form", "313"))
        self.comboBox.setItemText(3, _translate("Form", "912"))
        self.checkBox_4.setText(_translate("Form", "Добавить тело"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

