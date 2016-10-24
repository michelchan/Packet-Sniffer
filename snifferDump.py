from scapy.all import *

"""numPackets = 20
timeout = 5
packets = sniff(timeout=timeout)"""


def snifferDump(packets, filename):

    i = 0
    sys.stdout = open(filename, "w")
    for x in packets:
        # extract relevant info
        # proto = x[1].proto

        srcport = x[2].sport
        dstport = x[2].dport
        print "Packet # " + str(i)
        if x[1].version == 6:
            print x[1].sprintf("Protocol: %IPv6.nh%")
        else:
            print x[1].sprintf("Protocol: %IP.proto%")

        # determine packet type
        if srcport == 80 or dstport == 80:
            print "This is a HTTP packet: \n"
        elif srcport == 443 or dstport == 443:
            print "This is a HTTPS packet: \n"
        elif srcport == 53 or dstport == 53:
            print "This is a DNS packet: \n"
        else:
            print "This is not a recognizable packet: \n"

        # print packet
        x.show()
        i += 1
        print "\n=================================\n"

    # stop dumping and clean up
    sys.stdout.close()
    sys.stdout = sys.__stdout__
