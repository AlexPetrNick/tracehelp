import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from main import Ui_Form
from prog import *

class TiHe(QtWidgets.QMainWindow):
	def __init__(self):
		super(TiHe, self).__init__() 
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.init_UI()

	def init_UI(self):
		self.setWindowTitle("TraceHelp")
		self.ui.textEdit.setPlaceholderText("Тут должны отображатся текст")
		self.ui.pushButton.setText("Обзор")
		self.ui.pushButton_2.setText("Генерировать")
		self.ui.lineEdit.setText("Выберите файл")
		self.ui.pushButton.clicked.connect(self.show_sscc) 
		self.ui.label.setText("Текущий файл")

	def show_sscc(self,):
		"""Выбор файла для работы, установка root для self"""
		global work_file, current_file
		temp = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[0]
		file_name = temp.split("/")[-1]
		self.ui.lineEdit.setText(str(file_name))
		current_file = DocXML(file_name)
		with open(work_file, "w") as fs:
			os.chdir("into")
			fs.write(str(current_file.__dict__))
			os.chdir("..")

current_file = ''

work_file = "into/info_file.txt"


app = QtWidgets.QApplication([])
application = TiHe()
application.show()


sys.exit(app.exec())
