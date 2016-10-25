from scapy.all import *
import sys, getopt
from search import findKeyword


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




opts, args = getopt.getopt(sys.argv[1:], 'o:v',["sniff",
                                            "parse",
                                            "search",
                                            "html",
                                            "dns",
                                         ])

for opt, arg in opts:
    if opt == "--sniff":
        s = raw_input("Enter amount of time in seconds to sniff:")
        if s.isdigit():
            sniff(s)
        else:
            print "Must be a whole number"
    elif opt == "--parse":
        parse()
    elif opt == "--search":
        s = raw_input("Enter keyword or regex:")
        findKeyword(s)
    elif opt == "--html":
        html()
    elif opt == "--dns":
        dns()