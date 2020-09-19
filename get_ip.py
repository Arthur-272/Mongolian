import threading
import re
import subprocess

def getip(n,cmd):
    global ip
    temp=cmd + str(n)
    res= subprocess.Popen(("ping -n 1" + temp), shell =True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    res=res.stdout.read().decode()
    if 'Request time out.' in res or 'Destination host is unreachable.' in res:
        pass
    else:
        ip.append(temp)
        print(ip)
cmd="ipconfig"
cmd=subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
temp=re.findall('IPv4 Address.+: (.+)',cmd.stdout.read().decode())
print(temp)
temp=temp[0].rstrip()
print(temp)
temp=temp.split(".")
a1= int(temp[0])
a2= int(temp[1])
a3= int(temp[2])
cmd=str(a1) +","+str(a2)+","+str(a3)
ip=[]
for i in range(1,255):
    b=threading.Thread(name =i, target=getip, args=(i,cmd))
    b.daemon=False
    b.start()


