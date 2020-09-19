import threading
import re
import subprocess
import pysftp as sftp

def dictionary_attack(host):
    usrname=['root','admin','harsh','username']
    passwrd=['root','toor','1234','default']
    print("ff")
    for username in usrname:
        for password in passwrd:
            try:
                print(username,password)

            except:
                pass
dictionary_attack(host='127.0.0.1')
