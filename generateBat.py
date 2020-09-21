#!/usr/bin/env python3

def generateBat(user):
	f = open('windowsWallpaper.bat','wt')
	f.write('reg add "HKEY_CURRENT_USER\\Control Panel\\Desktop" /v Wallpaper /t REG_SZ /d C:\\Users\\'+user+'\\Desktop\\wallpaper.bmp /f \n')
	f.write('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters')
	f.close()