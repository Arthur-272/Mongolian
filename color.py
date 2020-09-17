from colorama import init, Fore, Back, Style
from termcolor import colored

init()

def print(string):
	print(colored(Fore.RED + string))
print("Radhey")