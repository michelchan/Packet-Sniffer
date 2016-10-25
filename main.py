import getopt

from scapy.all import *

from HTMLReconstructor import html
from dnsParser import dnsParser
from search import findKeyword
from sniff import sniff
from snifferDump import snifferDump


s = raw_input("Enter amount of time in seconds to sniff:")
if not s.isdigit():
    print "Must be a whole number"
    sys.exit(1)

packets = sniff(s)

opts, args = getopt.getopt(sys.argv[1:], 'o:v', ["parse",
                                                 "search",
                                                 "html",
                                                 "dns",
                                                 "help"
                                                 ])

for opt in opts:
    if opt[0] == "--parse":
        filename = raw_input("Enter file name to write to:")
        snifferDump(packets, filename)
    elif opt[0] == "--search":
        s = raw_input("Enter keyword or regex:")
        filename = raw_input("Enter the parse file to read from:")
        if os.path.isfile(filename):
            snifferDump(packets, filename)
        findKeyword(s, filename)
    elif opt[0] == "--html":
        html(packets)
    elif opt[0] == "--dns":
        filename = raw_input("Enter file name to write to:")
        dnsParser(packets, filename)
    elif opt[0] == "--help":
        print "--parse: takes filename and parses packets according to type of packets" \
              "--search: takes file name and keyword/regex, outputs packets that contain the keyword/regex" \
              "--html: takes and outputs the html" \
              "--dns: takes filename and outputs dns queries"
