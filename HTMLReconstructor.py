from scapy.all import *
import urllib2

def html(packets):

    for p in packets:
        try:
            load = p[3].load
            if "GET" in  load[0:4]:
                hostindex = load.index("Host:")
                host = load[hostindex:]
                # print host
                endhost = host.index("\r")

                fullhost = 'http://' + host[6:endhost] + load[4:hostindex-11];
                print fullhost

                last = fullhost.rindex('/')
                filename = ""
                if(fullhost[last+1:] != ''):
                    filename = fullhost[last+1:]
                else:
                    filename = host[6:endhost]+'.index.html'

                req = urllib2.Request(fullhost)
                f = open(filename,'w')
                f.write(urllib2.urlopen(req).read())
                f.close()
        except:
            continue
