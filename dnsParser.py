from scapy.all import *


def convertRaw(x):
    x[2].decode_payload_as(scapy.layers.dns.DNS)
    offset = 1
    if x[3].qdcount > 0:
        x[2 + offset].decode_payload_as(scapy.layers.dns.DNSQR)
        offset += 1
    elif x[3].ancount > 0:
        x[2 + offset].decode_payload_as(scapy.layers.dns.DNSRR)
        offset += 1


def getType(value):
    if int(value) == 1:
        return "A"
    if int(value) == 6:
        return "SOA"
    if int(value) == 28:
        return "AAAA"
    if int(value) == 5:
        return "CNAME"
    if int(value) == 15:
        return "MX"
    if int(value) == 2:
        return "NS"
    if int(value) == 12:
        return "PTR"
    if int(value) == 37:
        return "CERT"


def dnsParser(packets, filename):
    sys.stdout = open(filename, "w")
    i = 0
    for x in packets:

        # skip this packet if it is not an DNS packet
        if x[2].sport != 53 and x[2].dport != 53:
            i += 1
            continue

        # ensure that the contents are not read as raw
        if type(x[3]) == scapy.packet.Raw:
            try:
                convertRaw(x)
            except:
                sys.stderr.write("Error occured in converting packet %d\n" % i)
                i += 1
                continue

        """# print packet
        print x[3].id
        print x.show()"""

        # print request / response
        print "Packet " + str(i)
        numQueries = int(x[3].qdcount)
        numAns = int(x[3].ancount)
        if numQueries > 0:  # there is a query record
            qType = getType(x[4].qtype)
            qName = str(x[4].qname)
            print "DNS query of type " + qType + " for " + qName
        if numAns > 0:  # there is an answer record
            a = 1
            while a <= numAns:
                qType = getType(x[4 + a].type)
                qName = str(x[4 + a].rrname)
                qResult = str(x[4 + a].rdata)
                print "DNS response of type " + qType + " for " + qName + " returned " + qResult
                a += 1

        # advance
        i += 1
        print "\n=================================\n"

    sys.stdout = sys.__stdout__


""" Debugging lines
sys.stdout = open("DNSdump.txt", "w")
count = 20
# packets = sniff(filter="udp", timeout=5)

packets = rdpcap("packets.cap")
# wrpcap("programPackets.cap", packets)
packets.show()
print "\n==========================\n"""
