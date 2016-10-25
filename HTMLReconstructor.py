from scapy.all import *
import urllib2

def html(packets):

    for p in packets:
        try:
            load = p[3].load
            if "GET" in  load[0:4]:
                print load
        except:
            continue
