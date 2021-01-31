import os
import xml.etree.ElementTree as ET
import math
import time 
import calendar

from datetime import datetime

class XML:
    def __init__(self, file):
        self.file = file                                        
        self.root = get_root(file)                              #Получение корневого тега 
        self.list_tags = get_list_tags(self.root)               #Лист тэгов
        if "operation_result" in self.list_tags:
            self.type_file = "Ответ(тикет)"
        else:
            self.type_file = "Файл для отправки"
"""def get_parent(current_file, tag):
    tree = ''
    root = get_root(current_file)
    istina = True
    while(istina):
        temp2 = root.find('sscc')
        temp = root.findall('./')"""
        
def get_day_file(time_second):
    """Количество дней прошедших с последнего изменения файла"""
    data = time.localtime(time_second)      #Секунды с начало эпохи файлм
    data_mouth = data.tm_mon                #Месяц изменения файла
    data_day = data.tm_mday                 #День изменения файла

    second_now = time.time()                #Секунды текущие с начало эпохи файлм
    data_now = time.localtime(second_now)                
    data_mouth_now = data_now.tm_mon                #Месяц текущии
    data_day_now = data_now.tm_mday                 #День текущии
    count_day_now_month = calendar.monthrange(data_now.tm_year, data_now.tm_mon)[1]

    out_mon = data_mouth_now - data_mouth
    out_day = data_day_now - data_day
    if out_mon == 0:
        day = out_day
    else:
        day = (count_day_now_month - data_day) + data_day_now
    return day

def divide_with_symbol(st, sym):
    """Разделяет заданную строку st заданным символом sym"""
    st = ''.join(st.split())
    list = st.split(sym)
    print(list)
    return list
        
def get_root(file):
    """Попытка вернуть дерево в начальном расположении(root)"""
    try:
        tree = ET.parse(file)
        root = tree.getroot()
    except ErrorNotRootFile as er:
        print(er)
    return root
    
def get_list_current_files(*list_expan, show_scr = False, all_file = False, c_day = 0):
    """Возвращает список заданных файлов, 
    на входе список расширении, показать на экране show_scr, показать все файлы all_file
    (c_day не работает),c_day количество дней, прошедших с последнего 
    изменения файла (поумолчанию 0)"""
    count = 1
    list_dir = os.listdir()
    list_output = []
    for item in list_dir:
        if all_file:
            list_output.append(item)
            if show_scr:
                print(str(count)+ ". " + item + ".")
                count += 1
        else:
            day_edit_file = get_day_file(os.path.getmtime(item))
            if get_day_file(os.path.getmtime(item)) <= c_day:
                input_exp = os.path.splitext(item)[1].replace(".","")
                if input_exp in list_expan[0] and os.path.isfile(item):
                    list_output.append(item)
                    if show_scr:
                        print(str(count) + ". " + item + f" (Файл загружен {day_edit_file} дней назад)")
                        count += 1
    return list_output

def is_int(string):
    """Проверка на целочисленное"""
    out = True
    try:
        enter = int(string)
    except:
        out = False
    return out
    
def is_true_xml(xml):
    """Проверка на правильность xml файла"""
    out = True
    try:
        tree = ET.parse(xml)
        root = tree.getroot()
    except:
        out = False
    return out
        
    
def get_list_tags(root):
    """Возвращает все тэги из файла"""
    list = []
    for item in root.iter():
        if item.tag not in list:
            list.append(item.tag)
    return list

def get_sscc_sgtin(root, sscc = False, sgtin = False):
        """Получить sscc или sgtin"""
        text_all = ""
        if sscc:
            text_all += "SSCC\n"
            for item in root.iter("sscc"):
                text_all += item.text + "\n"
        if sgtin:
            text_all += "SGTIN\n"
            for item in root.iter("sgtin"):
                text_all += item.text + "\n"
        return text_all

def serialize_to_file(file):
    curr_file = DocXML(file)
    

def copy_in_variable(text):
    a = text
    print(a)
    return a


class UserDB:
    connect = None
    def __init__(self, databasename, in_user, my_password, host_con):
        self.databasename = databasename
        self.in_user = in_user
        self.my_password = my_password
        self.host_con = host_con

    def return_param(self):
        dict_temp = {
        "databasename" : databasename,
        "in_user" : in_user,
        "my_password" : my_password,
        "host_con" : host_con
        }
        return dict_temp

    def init_connect(self, conn):
        connect = conn

    def disinit_connect(self, conn):
        connect = conn
        connect.close()
