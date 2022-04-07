import ipaddress
import socket, re, threading, time
import pandas as pd
import numpy as np
from array import array
import time
start = time.time()
    

def inMo(aMo):
    print('aMo', aMo)
    if str(aMo) != '[]':
        return True
    else:
        return False

def getForDns(listOfEm, ddict):
    n = 0
    # Forward DNS
    # for i in listOfEm:
    #     print(i)


    
        #print('c', c)
    for site in listOfEm:
        try :
            dns = socket.getaddrinfo(site, 443, type=socket.SOCK_STREAM)
        except:
            pass
        mo = ipAddressFormat.findall(str(dns))
        gg[site] = mo
        moo = dnsIndicator.findall(site)
        inn = sitesAsArrayList.index(site)
        #ipAddresses.append(mo)
        ddict[sitesAsArrayList[inn]] = mo
        if len(mo) > 1:
            for t in mo:
                ipAddresses.append(t)
                
        else:
            ipAddresses.append(str(mo).strip("['\"\']"))
        #ipAddresses.append(int(mo))
        
    endingIndexIP = ((len(ipAddresses)/2)-1)
    for ii in range(len(ipAddresses)):
        if ii >= endingIndexIP:
            ipAsArray2.append(ipAddresses[ii])

        elif ii < endingIndexIP:
            ipAsArray1.append(ipAddresses[ii])


    #Reverse DNS
def revDNS(listOfEm, ddict):
    for ip in listOfEm:
        try:
            rDnsDomain = socket.getfqdn(ip)
        except:
            pass
        site = sitesAsArray[listOfEm.index(ip)]
        inn = sitesAsArrayList.index(site)
        #ddict[sitesAsArrayList[listOfEm.index(ip)]] = rDnsDomain
        ddict[ip] = rDnsDomain

def findMatch(ar, ar2):
    indexx = 0
    for key in ar:
        try:
            if ar2[indexx] in ar.get(key):
                ggg[key] = ar.get(key)
        except:
            pass
        indexx = indexx + 1

domains = pd.read_csv('domains.tsv', sep='\t')
sites = domains['domain']
sitesAsArray = np.asarray(sites)  # Extracting sties

sitesAsArrayList = sitesAsArray.tolist()
sitesAsArray1 = []
sitesAsArray2 = []
ipAsArray1 = []
ipAsArray2 = []
ipAddresses = []
forDNS1 = dict()
forDNS2 = dict()
ipAddressFormat = re.compile(r'\d+\.\d+\.\d+\.\d+')
dnsIndicator = re.compile(r'\d')
ipDict = dict()
ipDNS = dict()
ipDNS2 = dict()
gg = dict()
ggg = dict()
endingIndex = (len(sitesAsArray)/2)-1
endingIndexIP = (len(ipAddresses)/2)-1


t1 = threading.Thread(target=getForDns, args=(sitesAsArray1, forDNS1,))
t2 = threading.Thread(target=getForDns, args=(sitesAsArray2, forDNS2,))
t3 = threading.Thread(target=revDNS, args=(ipAsArray1, ipDNS,))
t4 = threading.Thread(target=revDNS, args=(ipAsArray2, ipDNS2,))



for i in range(len(sitesAsArray)):
    if i >= endingIndex:
        sitesAsArray2.append(sitesAsArray[i])
        #ipAsArray2.append(ipAddresses[i])

    elif i < endingIndex:
        sitesAsArray1.append(sitesAsArray[i])
        #ipAsArray1.append(ipAddresses[i])


# for x in sitesAsArray:
#     dns = socket.getaddrinfo(x, 443, type=socket.SOCK_STREAM)

t1.start()
t2.start()
t1.join()
t2.join()
t3.start()
t4.start()
t3.join()
t4.join()



mainDNS = dict(forDNS1, **forDNS2)
ipDict = dict(ipDNS, **ipDNS2)
end = time.time()
howLong = end - start
#Calling ggg
t5 = threading.Thread(target=findMatch, args=(gg, ipDict,))
t5.start()
t5.join()

print('Domains: ', end=f'\n{sitesAsArray}')
print()
print()
print('Forward DNS', end=f'\n{mainDNS}')
print()
print()
print('IP Addresses', end=f'\n{ipAddresses}')
print()
print()
#print(type(ipAddresses))
print("Rev DNS", end=f'\n{ipDict}')

print()
print()
print("dic", end=f'\n{gg}')
print()
print()
print(f'This program completed in {round(howLong, 2)} seconds')
# print(len(sitesAsArray1))
# print(len(sitesAsArray2))