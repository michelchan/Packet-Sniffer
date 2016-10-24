from scapy.all import *

def convertRaw(x):
    x[2].decode_payload_as(scapy.layers.dns.DNS)
    offset = 1
    if x[3].qdcount > 0:
        x[2+offset].decode_payload_as(scapy.layers.dns.DNSQR)
        offset += 1
    elif x[3].ancount > 0:
        x[2+offset].decode_payload_as(scapy.layers.dns.DNSRR)
        offset += 1
    elif x[3].nscount > 0:
        x[2+offset].decode_payload_as(scapy.layers.dns.DNSQR)
        offset += 1
    elif x[3].arcount > 0:
        x[2+offset].decode_payload_as(scapy.layers.dns.DNSQR)
        offset += 1



sys.stdout = open("DNSdump.txt", "w")

count = 20
packets = sniff(filter="udp", timeout = 10)
packets.nsummary()

print "\n==========================\nStart parsing\n"

i = 0
for x in packets:

    # skip this packet if it is not an DNS packet
    if x[2].sport != 53 and x[2].dport != 53:
        i += 1
        continue

    # ensure that the contents are not read as raw
    print "Packet " + str(i)
    if type(x[3]) == scapy.packet.Raw:
        try:
            convertRaw(x)
        except:
            print "Error occured in converting packet " + str(i)
            i += 1
            continue

    # print packet
    print x[3].id
    print x.show()
    i += 1
    print "\n=================================\n"

sys.stdout = sys.__stdout__
