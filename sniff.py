from scapy.all import *


def sniff(time):
    print "sniff " + time
    packets = scapy.all.sniff(timeout=int(time))
    packets.show()
    wrpcap('dump.cap', packets)
    return packets
