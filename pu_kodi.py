import os
import time
from pathlib import Path

def run_kodi():
    os.system('sh /home/user/kodi.sh')


def check_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    last_line = lines[-1]
    last_line = last_line.rstrip()
    return last_line

def read_temp():
    with open('temp_for_kodi_script', 'r') as f:
        lines = f.readlines()
        line = lines[-1].rstrip()
    return line

def write_temp(string):
    with open('temp_for_kodi_script', 'a') as f:
        f.write('\n' + string)

def parsing(string, check_string):
    res = []
    lst = string.split()
    if lst[0] == check_string:
        res.append(True)
    else:
        res.append(False)
    head, sep, tail = lst[1].partition('.')
    res.append(int(head))
    return res



if __name__ == "__main__":
    file_name = '/usr/share/hassio/homeassistant/for_py_script.txt'
    temp_file = Path("/home/user/temp_for_kodi_script")
    check_string = 'start_kodi'
    if temp_file.is_file():
        pass
    else:
        write_temp('0')
    while True:
        temp_string = read_temp()
        line = check_file(file_name)
        par_line_lst = parsing(line, check_string)
        if par_line_lst[0]:
            if int(temp_string) < par_line_lst[1]:
                run_kodi()
                print('RUN KODI NOW')
                write_temp(str(par_line_lst[1]))
        time.sleep(2)
        print('OK')

