#!/usr/bin/env python3

import blowfish
from cryptography.fernet import Fernet
import os
from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

user = os.getlogin()
keys_folder = '/tmp/KEYS/'

def get_details(file):
	file = file.split('/')
	length = len(file)
	filename = file[length-1]
	path = ''
	for i in range(length-1):
		path += file[i] + "/"
	return [path, filename]

def decryptKey():
	f = open(keys_folder + 'private.r4dh3y','rb')
	pemdata = f.read()
	f.close()

	f = open(keys_folder + 'password.r4dh3y','rb')
	password = f.read()
	f.close()

	privateKey = serialization.load_pem_private_key(
		data=pemdata,
		password=password,
		backend=default_backend()
	)

	f = open(keys_folder + 'symmetricKey.r4dh3y','rb')
	data = f.read()
	f.close()
	plain_text = privateKey.decrypt(
		data,
		padding=padding.OAEP(mgf=padding.MGF1(
				algorithm=hashes.SHA256()
			),
			algorithm=hashes.SHA256(),
			label=None
		)
	)
	os.remove(keys_folder + 'symmetricKey.r4dh3y')
	f = open(keys_folder + 'symmetricKey.key','wb')
	f.write(plain_text)
	f.close()

	os.remove(keys_folder + 'private.r4dh3y')
	os.remove(keys_folder + 'public.r4dh3y')
	os.remove(keys_folder + 'password.r4dh3y')