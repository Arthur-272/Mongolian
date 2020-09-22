#!/usr/bin/env python3

import linuxPayload, linuxKeyFileEncryptor

def main():
	linuxPayload.main()
	linuxKeyFileEncryptor.encryptKey()

if __name__ == '__main__':
	main()