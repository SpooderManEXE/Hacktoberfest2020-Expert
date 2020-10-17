#!/usr/bin/python

from scapy.all import *



def findDNS(p):
	if p.haslayer(DNS):
		print p[IP].src, p[DNS].summary()
		#see the source to which we have to reach to get dns request


sniff(prn=findDNS)
