import netifaces as ni
import ipaddress, winreg as wr
from getmac import get_mac_address
from pprint import pprint


'''
1. The answer to the first question is 
    output:
        
jwjjw@DESKTOP-V5QRLF1 MINGW64 ~/Desktop/Text_Files/NetworkManagement/hw
$ ipconfig

Windows IP Configuration


Ethernet adapter Ethernet:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Ethernet adapter vEthernet (WSL):

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::b555:e5b5:8c51:db69%46
   IPv4 Address. . . . . . . . . . . : 172.23.144.1
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :

Wireless LAN adapter Wi-Fi:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : domain_not_set.invalid

Wireless LAN adapter Local Area Connection* 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Local Area Connection* 9:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Wi-Fi 2:

   Connection-specific DNS Suffix  . : belhaven.edu
   Link-local IPv6 Address . . . . . : fe80::68cc:e573:2d7f:6751%10
   IPv4 Address. . . . . . . . . . . : 192.168.177.138
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . : 192.168.176.1

'''
def get_connection_name_from_guid(iface_guids):
    iface_names = ['(unknown)' for i in range(len(iface_guids))]
    reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
    reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
    for i in range(len(iface_guids)):
        try:
            reg_subkey = wr.OpenKey(reg_key, iface_guids[i] + r'\Connection')
            iface_names[i] = wr.QueryValueEx(reg_subkey, 'Name')[0]
        except FileNotFoundError:
            pass
    return iface_names

def getInterfaces():
    #aa = {}
    
    """Return a list of all the interfaces on this host

        Args: None

        Returns: (list) List of interfaces for this host
    """
    ifaces = ni.interfaces()
    

    inter = str(ifaces)

    a = inter.split(',')

    for i in a:
        aaa = i.strip() #removes whitespace (has to be done first)
        cd = aaa.strip("[,],'")
        dc = cd.strip('"')
        interfaces.append(dc)
    
    return(interfaces)

def get_mac(t):
    # t will represent the interface
    macAddrIndex = ni.AF_LINK
    dd = ni.ifaddresses(together[t])
    addresses.append(dd[macAddrIndex][0]['addr'])

def get_ips(u):
    # u will be all interfaces collected so far
    uu = []
    uu.append(together[u])
    ip4AddIndex = ni.AF_INET
    ip6AddIndex = ni.AF_INET6
    ip = dict()
    
    for i in uu:

        ip.clear()
        tt = ni.ifaddresses(i)
        collection.append(tt)
        if ip4AddIndex in tt.keys():
            #ip4.append(tt)
            ad = tt[ip4AddIndex][0]['addr']
            b = ipaddress.ip_address(ad)
            a = f'ipaddress.IPv4Address({b})'
            ip['v4'] = (a)
        elif ip6AddIndex in tt.keys():
            #ip6.append(tt)
            da = tt[ip6AddIndex][0]['addr']
            e = ipaddress.ip_address(da)
            f = f'ipaddress.IPv6Address({e})'
            ip['v6'] = f
    print('  ',u) 
    return ip

def get_netmask(interf):
    xx = []
    xx.append(together[interf])
    ip4AddIndex = ni.AF_INET
    ip6AddIndex = ni.AF_INET6
    net = dict()

    for i in xx:
    
        net.clear()
        tt = ni.ifaddresses(i)
        #collection.append(tt)
        if ip4AddIndex in tt.keys():
            #ip4.append(tt)
            ad = tt[ip4AddIndex][0]['netmask']
            #b = ipaddress.ip_address(ad)
            a = f"ipaddress.IPv4Address('{ad}')"
            net['v4'] = (a)
        elif ip6AddIndex in tt.keys():
            #ip6.append(tt)
            da = tt[ip6AddIndex][0]['netmask']
            #e = ipaddress.ip_address(da)
            f = f"ipaddress.IPv6Address('{da}')"
            net['v6'] = f
        print('  ',interf)
        return net

def get_network(iName):
    pertainingNetworks = []
    pertainingNetworks.append(together[iName])
    ip4AddIndex = ni.AF_INET
    ip6AddIndex = ni.AF_INET6
    networks = dict()

    for i in pertainingNetworks:
    
        networks.clear()
        tt = ni.ifaddresses(i)
        #collection.append(tt)
        if ip4AddIndex in tt.keys():
            #ip4.append(tt)
            ad = tt[ip4AddIndex][0]['broadcast']
            #b = ipaddress.ip_address(ad)
            a = f"ipaddress.IPv4Address('{ad}')"
            networks['v4'] = (a)
        elif ip6AddIndex in tt.keys():
            #ip6.append(tt)
            da = tt[ip6AddIndex][0]['broadcast']
            #e = ipaddress.ip_address(da)
            f = f"ipaddress.IPv6Address('{da}')"
            networks['v6'] = f
        print('  ', iName)
        return networks
print()
p = 0
  
together = dict()
interfaces = []
getInterfaces()  
addresses = []
x = ni.interfaces()
aaa = get_connection_name_from_guid(x)
namedInterfaces = []
collection = []

for c in aaa:
    if c == '(unknown)':
        break
    namedInterfaces.append(c)

for j in aaa:
    together[j] = interfaces[p]
    p += 1

# Interfaces
print("Interfaces:")
for i in namedInterfaces:
    get_mac(i)
addresses = list(filter(None, addresses))
print('  ', namedInterfaces)
print()

# MAC Addresses
print("MAC Addresses:")
print('  ',addresses)
print()

# Interfaces
print('Interfaces and their IP addresses:')
for y in namedInterfaces:
    ll = get_ips(y)
    print('    ',ll)
print()

# Netmask
print('Netmask')
for z in namedInterfaces:
    mm = get_netmask(z)
    print('    ', mm)
    print()

# Networks
print('Networks')
for s in namedInterfaces:
    kk = get_network(s)
    print('    ', kk)