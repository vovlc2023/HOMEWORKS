
class My_file:
    def __init__(self, name):
        self.name = name
        with open(self.name, encoding='utf-8') as file1:
            self.file_content = file1.read()
            self.file_len = len(self.file_content.split('\n'))

    def set_file_str_len(self):
        with open(self.name, encoding='utf-8') as file1:
            self.file_len = len(file1.read().split('\n'))

    def set_file_content(self):
        with open(self.name, encoding='utf-8') as file1:
            self.file_contetnt = file1.read()

    def get_file_content(self):
        return self.file_contetnt
    def get_name(self):
        return self.name

def save_file_list(files_list, file_name):
    str_for_save = ''
    file_list.sort(key = lambda x: x.file_len)
    with open(file_name, 'w', encoding='utf-8') as new_file:
        for file in files_list:
            str_for_save = file.name + '\n' + str(file.file_len) + '\n' + file.file_content + '\n'
            new_file.write(str_for_save)

f1 = My_file('1.txt')
f2 = My_file('2.txt')
f3= My_file('3.txt')
file_list = [f1, f2, f3]
save_file_list(file_list, 'result_file.txt')