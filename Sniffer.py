from scapy.all import *

numPackets = 20
timeout = 5

# packets = sniff(count=numPackets)
packets = sniff(timeout=timeout)

sys.stdout = open("dump.txt", "a")
for x in range(0, numPackets - 1):
    #extract relevant info
    proto = packets[x][1].proto
    srcport = packets[x][2].sport
    dstport = packets[x][2].dport
    print "Packet# \n" + str(x)

    # determine packet type
    if srcport == 80 or dstport == 80:
        print "This is a HTTP packet: \n"
    elif srcport == 443 or dstport == 443:
        print "This is a HTTPS packet: \n"
    elif srcport == 40 or dstport == 40:
        print "This is a DNS packet: \n"
    else:
        print "This is not a recognizable packet: \n"

    # print packet
    packets[x].show()

    print "\n=================================\n"

sys.stdout.close()
sys.stdout = sys.__stdout__


