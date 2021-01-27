import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from main import Ui_Form
from prog import *
import json


class AppEncoder(json.JSONEncoder):
	def try_encode(self, obj):
		if isinstance(obj, DocXML):
			return obj.__doc__
		return json.JSONEncoder.try_encode(self, obj)

class TiHe(QtWidgets.QMainWindow):
	def __init__(self):
		super(TiHe, self).__init__() 
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.init_UI()

	def init_UI(self):
		self.setWindowTitle("TraceHelp")
		self.ui.textEdit.setPlaceholderText("Тут отображаются SSCC")
		self.ui.textEdit_4.setPlaceholderText("Тут отображаются SGTIN")
		self.ui.pushButton.setText("Обзор")
		self.ui.pushButton_2.setText("Генерировать")
		self.ui.lineEdit.setText("Выберите файл")
		self.ui.pushButton.clicked.connect(self.show_sscc) 
		self.ui.pushButton_2.clicked.connect(self.generate)
		self.ui.comboBox.isEnabled(False)
		self.ui.comboBox_2.isEnabled(False)
		if self.ui.checkBox_3.isChecked():
			self.ui.comboBox.isEnabled(True)
		if self.ui.checkBox_4.isChecked():
			self.ui.comboBox.isEnabled(True)

	def show_sscc(self):
		"""Выбор файла для работы, установка root для self"""
		global work_file, current_file, dict_temp
		temp = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[0]
		file_name = temp.split("/")[-1]
		self.ui.lineEdit.setText(str(file_name))
		current_file = DocXML(file_name)
		dict_temp = current_file.__dict__
		with open(work_file, "w") as fs:
			os.chdir("into")
			fs.write(str(dict_temp))
			os.chdir("..")

		row_info = self.ui.textEdit_5
		row_text = current_file.type_file

		row_info.setText(row_text)
		


	def generate(self, a):
		dict_codes = {}
		text_to_box = ''
		col_sgtin = self.ui.textEdit_4
		col_sscc = self.ui.textEdit
		global current_file
		sscc_i = self.ui.checkBox_2.isChecked()
		print(f"sscc_i = {sscc_i}")
		sgtin_i = self.ui.checkBox.isChecked()
		print(f"sgtin_i = {sgtin_i}")
		dict_codes = current_file.get_codes(sscc = sscc_i, sgtin = sgtin_i)
		text_to_box = "SSCC\n"
		print(type(dict_codes))
		for item in dict_codes["sscc"]:
			text_to_box += str(item) + "\n"
		col_sscc.setText(text_to_box)
		text_to_box = "SGTIN\n"
		for item in dict_codes["sgtin"]:
			text_to_box += str(item) + "\n"
		col_sgtin.setText(text_to_box)




current_file = ''
dict_temp = {}
work_file = "into_try.json"


app = QtWidgets.QApplication([])
application = TiHe()
application.show()


sys.exit(app.exec())
