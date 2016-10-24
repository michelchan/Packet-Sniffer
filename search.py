import re


def findKeyword(keyword):
    file = 'dump.txt'

    with open(file, 'r') as f:
        dump = f.readlines()

    packets = []
    packet = ""
    found = False
    for line in dump:
        # if re.search(keyword, line):
        #     withNewLine = line + "\n"
        #     packet += withNewLine
        #     print withNewLine
        # if re.match("=================================", line):
        #     packets.append(packet)
        #     packet = ""

        if re.match("=================================", line):
            if found:
                packets.append(packet)
            packet = ''
            found = False
        else:
            if re.search(keyword, line):
                found = True
            withNewLine = line + "\n"
            packet += withNewLine

    output = open("searchresults.txt", "w")
    for i in packets:
        output.write("%s\n" % i)

    print "All packets containing " + keyword + " are available in 'searchresults.txt'"
