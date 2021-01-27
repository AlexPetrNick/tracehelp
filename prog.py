from adds import *
from errors import *
     

class DocXML(XML):
    def get_codes(self, sscc = False, sgtin = False):
        """Получить sscc или sgtin"""
        list_sscc = []
        list_sgtin = []
        temp_dict = {"sscc":[], "sgtin":[]}
        if sscc:
            for item in self.root.iter("sscc"):
                list_sscc.append(item.text)
        temp_dict['sscc'] = list_sscc
        if sgtin:
            for item in self.root.iter("sgtin"):
                list_sgtin.append(item.text)
        temp_dict['sgtin'] = list_sgtin
        return temp_dict
    def get_info(self):
        """Получить информацию какие ошибки, и их количество"""
        err_dict = {}
        err_dict_out = {}
        if self.type_file == "Ответ(тикет)":
            error_iter = self.root.iter("error_code")
            for i in error_iter:
                if i.text not in err_dict.keys():
                    err_dict[i.text] = ["1"]
                else:
                    err_dict[i.text].append("1")
        for key in err_dict:
            temp = len(err_dict[key])
            err_dict_out[key] = temp
        return err_dict_out

    
if __name__ == "__main__":
    os.chdir(r'C:\Users\alek.petrov\Downloads')
    truth = True
    truth2 = True
    print("Hello Alex")
    curr_dir = (os.getcwd()).split('\\')[-1]
    print(f"Текущая директория {curr_dir}")
    #expan = input("Введите необходимые расширения файлов через запятую: ")
    #list_expan = divide_with_symbol(expan, ',')
    #print(list_expan)
    list_expan = 'xml'
    work_list = get_list_current_files(list_expan, show_scr = True, c_day = 0)
    while(truth):
        while(truth2):
            curr = input("Выберие файл: ")
            truth2 = not is_int(curr)
        curr_num = int(curr) - 1
        current_file = work_list[curr_num]
        truth = not is_true_xml(current_file)
        if truth == True:
            truth2 = True 
    print("________________________________________________________")
    print()
    print("                   " + current_file + "                          ")
    print("________________________________________________________")
    curr_xml = DocXML(current_file)
    
    print(curr_xml.get_codes(sscc = True))
    tempdict = curr_xml.get_info()
    print(tempdict)
