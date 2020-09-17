import os
from get_ip import getIP
from get_os import getos

def dir(path):
    try:
        lst = os.listdir(path)
        for i in range(len(lst)):
            lst[i] = path + '/' + lst[i]
            dir(lst[i])
    except:
        print(path)

dir('/home/kali/Desktop')
