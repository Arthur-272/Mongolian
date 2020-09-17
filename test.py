import os

def dir(path):
    try:
        lst = os.listdir(path)
        for i in range(len(lst)):
            lst[i] = path + '/' + lst[i]
            dir(lst[i])
    except:
        print(path)

dir('/home/kali/Desktop')
