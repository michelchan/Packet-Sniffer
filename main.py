def sniff(time):
    print "sniff"

def parse():
    print "parse"

def search(keyword):
    print "search"

def html():
    print "html"

def dns():
    print "dns"

import sys, getopt

opts, args = getopt.getopt(sys.argv[1:], 'o:v',["sniff=",
                                            "parse",
                                            "search=",
                                            "html",
                                            "dns",
                                         ])

for opt, arg in opts:
    if opt == "--sniff":
        sniff(arg)
    elif opt == "--parse":
        parse()
    elif opt == "--search":
        search(arg)
    elif opt == "--html":
        html()
    elif opt == "--dns":
        dns()