#!/usr/bin/env python3

import threading
import subprocess
import re

flag = False

def returnIP():
    global ip, flag
    while True:
        if flag:
            return ip
        else:
            pass

def task(n, cmd):
    global ip, flag
    temp = cmd + str(n)
    res = subprocess.Popen(("ping -c 1 " + temp), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    res = res.stdout.read().decode()
    if 'Destination Host Unreachable' in res or 'Request Timed Out' in res:
        pass
    else:
        ip.append(temp)
    if n == 254:
        flag = True

def getIP(host_os):
    if host_os == 'Linux':
        cmd = 'sudo ifconfig'
        cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.read()
        temp = re.findall('inet (.+)  netmask', str(cmd))
        temp = temp[0].split('.')
        network = temp[0] + "."+ temp[1] + "." + temp[2] + "."
        ip = []
        for i in range(1,255):
            t = threading.Thread(name = i, target = task, args = (i, network))
            t.daemon = False
            t.start()
    elif host_os == 'Windows':
        cmd = 'ipconfig':
        cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.read()
        cmd = re.findall('IPv4 Address .+ : (.+)')
        temp = temp[0].split('.')
        network = temp[0] + '.' + temp[1] + '.' + temp[2] + '.'
        ip = []
        for i in range(1,255):
            t = threading.Thread(name = i, target = task, args = (i, network))
            t.daemon = False
            t.start()
    return returnIP()
