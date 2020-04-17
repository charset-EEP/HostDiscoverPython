#!/usr/bin/python3

import sys
from scapy.all import *
conf.verb=0

print("Hosts Vivos")
for ip in range(1,255):
    iprange = str(sys.argv[1])+"."+str(ip)
    pIP=IP(dst=iprange)
    pkg=pIP/ICMP()
    resp,noresp=sr(pkg,timeout=1)
    for resposta in resp:
        print (resposta[1][IP].src)
