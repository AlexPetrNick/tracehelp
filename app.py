import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from main import Ui_Form
from prog import *
import json
import re
import psycopg2



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
		self.ui.pushButton_2.setEnabled(False)
		self.ui.lineEdit.setText("Выберите файл")
		self.ui.pushButton.clicked.connect(self.show_sscc) 
		self.ui.pushButton_2.clicked.connect(self.generate)
		self.ui.checkBox_4.setEnabled(False) 	#Чек на добавление тела
		self.ui.comboBox.setEnabled(False)
		self.ui.checkBox_5.setEnabled(False)  #Чек бокс на SSCC
		self.ui.checkBox_6.setEnabled(False)  #Чек бокс на SGTIN
		self.ui.checkBox_3.clicked.connect(self.click_event)
		self.ui.checkBox_4.clicked.connect(self.click_event)
		self.ui.pushButton_3.clicked.connect(self.get_doc)
		self.ui.checkBox_7.setEnabled(False) #Чек на wrapper

		self.ui.checkBox_7.clicked.connect(self.out_in_wrapper)
		self.ui.pushButton_3.setEnabled(False)



	@QtCore.pyqtSlot()	
	def connect_to_databases(self):
		port1 = "61532"
		host1 = "192.168.100.213"
		db = "itrack2"
		name1 = "itrack"
		pa = "itrack"
		global my_db, connect
		try:
			connect = psycopg2.connect(dbname=db,user=name1,password=pa,host=host1,port = port1)
			self.change_color()
			self.ui.pushButton_3.setEnabled(True)
		except:
			print("Fail")


	@QtCore.pyqtSlot()	
	def disconnect_to_databases(self):
		global connect
		connect.close()
		self.ui.pushButton_3.setEnabled(False)
		self.change_color()

								
	def change_color(self):
		global connect
		if connect.closed == 0:
			self.ui.comboBox_2.setStyleSheet("background-color: green;\n"
"color: gray;")
		else:
			self.ui.comboBox_2.setStyleSheet("background-color: red;\n"
"color: gray;")


	def show_sscc(self):
		"""Выбор файла для работы, установка root для self"""
		global work_file, current_file, dict_temp
		temp = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[0]
		file_name = temp.split("/")[-1]
		self.ui.lineEdit.setText(str(file_name))
		current_file = DocXML(file_name)
		dict_temp = current_file.__dict__
		if dict_temp != '':
			self.ui.pushButton_2.setEnabled(True)
		with open(work_file, "w") as fs:
			os.chdir("into")
			fs.write(str(dict_temp))
			os.chdir("..")

	def func_for_generate_sscc_sgtin(self, dictionary):
		dict_codes = dictionary
		if len(dict_codes["sscc"]) >= 1:
			print("success")
			self.ui.checkBox_5.setEnabled(True)
			self.ui.checkBox_7.setEnabled(True)
			text_to_box = "SSCC\n"
			for item in dict_codes["sscc"]:
				text_to_box += str(item) + "\n"
			self.ui.textEdit.setPlainText(text_to_box)
		else:
			text_to_box = ''
			self.ui.textEdit.setEnabled(False)
			self.ui.checkBox_5.setEnabled(False)
			self.ui.checkBox_7.setEnabled(False)
		if len(dict_codes["sgtin"]) >= 1:
			print("success!!!")
			self.ui.checkBox_6.setEnabled(True)
			self.ui.checkBox_7.setEnabled(True)
			text_to_box = "SGTIN\n"
			for item in dict_codes["sgtin"]:
				text_to_box += str(item) + "\n"
			self.ui.textEdit_4.setPlainText(text_to_box)
		else:
			text_to_box = ''
			self.ui.textEdit_4.setEnabled(False)
			self.ui.checkBox_6.setEnabled(False)
			if self.ui.checkBox_7.isEnabled():
				self.ui.checkBox_7.setEnabled(True)
			else:
				self.ui.checkBox_7.setEnabled(False)
		if self.ui.checkBox_5.isEnabled() or self.ui.checkBox_6.isEnabled():
			self.ui.checkBox_4.setEnabled(True)	

	def generate(self, a):
		"""Генерировать SSCC и SGTIN по галочке"""
		dict_codes = {}	
		text_to_box = ''
		col_sgtin = self.ui.textEdit_4
		col_sscc = self.ui.textEdit
		self.ui.checkBox_4.setEnabled(False) 
		col_sgtin.clear()
		col_sscc.clear()
		global current_file
		sscc_i = self.ui.checkBox_2.isChecked()
		sgtin_i = self.ui.checkBox.isChecked()
		if current_file.type_file == "Файл для отправки":
			dict_codes = current_file.get_codes(sscc = sscc_i, sgtin = sgtin_i)
			self.func_for_generate_sscc_sgtin(dict_codes)
		elif current_file.type_file == "Ответ(тикет)":
			list_codes = current_file.root.iter("object_id")
			dict_codes = { "sscc" : [], "sgtin" : [] }
			for item in list_codes:
				if len(item) == 18:
					dict_codes["sscc"].append(item)
				elif len(item) == 27:
					dict_codes["sgtin"].append(item)
			self.func_for_generate_sscc_sgtin(dict_codes)
		else:
 			pass

	

	def click_event(self, what):
		check_one = self.ui.checkBox_3.isChecked()
		check_two = self.ui.checkBox_4.isChecked()
		if check_one or check_two:
			self.ui.comboBox.setEnabled(True)
		else:
			self.ui.comboBox.setEnabled(False)

	def get_doc(self):		
		pass

	def out_in_wrapper(self):
		l_cols = self.ui.textEdit
		r_cols = self.ui.textEdit_4

		i_sscc = True
		i_sgtin = True

		if self.ui.checkBox_7.isChecked():

			list_sgtin = r_cols.toPlainText().split("\n")
			list_sscc = l_cols.toPlainText().split("\n")
			text_sgtin = ''
			text_sscc = ''
			if  len(list_sscc) >= 1:
				text_sscc = 'SSCC\n'
				for item in list_sscc:
					if item != '' and item != "SSCC":
						text_sscc += "<sscc>" + str(item) + "</sscc>\n"
			if  len(list_sgtin) >= 3:
				text_sgtin = 'SGTIN\n'
				for item in list_sgtin:
					if item != '' and item != "SGTIN":
						text_sgtin += "<sgtin>" + str(item) + "</sgtin>\n"

			r_cols.setPlainText(text_sgtin)
			l_cols.setPlainText(text_sscc)
		else:
			text_sgtin = ''
			text_sscc = ''

			list_sscc = l_cols.toPlainText().split("<sscc>")
			list_sgtin = r_cols.toPlainText().split("<sgtin>")
			if len(list_sscc) >- 1:
				for i in range(0, len(list_sscc)):
					text_sscc += list_sscc[i].replace("</sscc>", "")
			if len(list_sgtin) >- 1:
				for i in range(0, len(list_sgtin)):
					text_sgtin += list_sgtin[i].replace("</sgtin>", "")

			r_cols.setPlainText(text_sgtin)
			l_cols.setPlainText(text_sscc)


connect = None
my_db = None

current_file = ''
dict_temp = {}
work_file = "into_try.json"


app = QtWidgets.QApplication([])
application = TiHe()
application.show()

application.ui.pushButton_4.clicked.connect(application.connect_to_databases)


application.ui.pushButton_5.clicked.connect(application.disconnect_to_databases)

sys.exit(app.exec())
