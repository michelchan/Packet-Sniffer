from scapy.all import *
import sys, getopt
from search import findKeyword
from snifferDump import snifferDump


def sniff(time):
    print "sniff " + time
    packets = scapy.all.sniff(timeout=int(time))
    packets.show()
    return packets


def parse():
    print "parse"


def html():
    print "html"


def dns():
    print "dns"


s = raw_input("Enter amount of time in seconds to sniff:")
if s.isdigit():
    sniff(s)
else:
    print "Must be a whole number"
packets = sniff(s)

opts, args = getopt.getopt(sys.argv[1:], 'o:v', ["parse",
                                                 "search",
                                                 "html",
                                                 "dns",
                                                 "help"
                                                 ])

for opt in opts:
    if opt == "--parse":
        filename = raw_input("Enter file name to write to:")
        snifferDump(packets, filename)
    elif opt == "--search":
        s = raw_input("Enter keyword or regex:")
        findKeyword(s)
    elif opt == "--html":
        html()
    elif opt == "--dns":
        dns()
    elif opt == "--help":
        print "--parse: takes "