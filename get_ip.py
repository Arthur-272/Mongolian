import threading
import subprocess
import socket

flag = False

def getIP():
    global ip, flag
    while True:
        if flag:
            return ip
        else:
            pass

def task(n, cmd):
    global ip, flag
    temp = cmd + str(n)
    res = subprocess.Popen(("ping -n 1 " + temp), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    res = res.stdout.read().decode()
    if 'Destination host unreachable.' in res or 'Request timed out.' in res:
        pass
    else:
        ip.append(temp)
    if n == 254:
        flag = True

temp = socket.gethostbyname(socket.gethostname())
temp = temp.split('.')
b1 = int(temp[0])
b2 = int(temp[1])
b3 = int(temp[2])
cmd = str(b1) + "."+ str(b2) + "." + str(b3) + "."
ip = []
for i in range(1,255):
    t = threading.Thread(name = i, target = task, args = (i, cmd))
    t.daemon = False
    t.start()