import nmap3

def getos(host):
    nm = nmap3.Nmap()
    res = nm.nmap_os_detection(host)
    return res[0]['osclass']['vendor']

#print(getos('10.0.2.8'))
