#!/usr/bin/env python3

import linuxKeyFileDecryptor
import linuxFileDecryptor

def main():
	linuxKeyFileDecryptor.decryptKey()
	linuxFileDecryptor.doit()

if __name__ == '__main__':
	main()