import os
import sys
import nmap
import winsound
import ipaddress

try:
    nm = nmap.PortScanner()
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)

mylist=(1,2,3,4,5)
#get targets from file

print('This program will scan ports 80 and 443 and output the results to the screen and a file you define \n')
filename=input("please type the name of the output file:\n ")
target = input("This will scan for ports 443 (https) and 80 (http) \nPlease list targets using / \nexample 10.0.0.1/24 \n Or type a single ip \nThis could take a long time please wait \n:")

def validate_ipaddress(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as errorCode:
        pass
        return False
def validate_ipnetwork(ip):
    try:
        ipaddress.ip_network(ip)
        return True
    except ValueError as errorCode:
        pass
        return False


def main():
#    ipaddr=target
    global target
    if '/' in target:
        if(validate_ipnetwork(target)==False):
            print("This is an invalid address.")
            target = input("Please enter an ip address:\n")

            
        else:
            print("IP address {} is valid".format(target))
            
    else: 
        if(validate_ipaddress(target)==False):
            print("This is an invalid address.")
            target = input("Please enter an ip address:\n")

            
        else:
            print("IP address {} is valid".format(target))
                


if __name__ == "__main__":
    main()
    
winsound.PlaySound('C:\Windows\media\tada.wav',1)


#nm.scan(target, '80,443')
nm=nmap.PortScanner()
nma=nmap.PortScannerAsync()
def callback_result(host, scan_result):
    print('---------------------')
    print (host, scan_result)

nm.scan(hosts=target, arguments="--open -p 80,443")
#while nma.still_scanning():
#    print("Waiting >>>>")
#    nma.wait(2)

for host in nm.all_hosts():
     print('----------------------------------------------------')
     print('Host : %s (%s)' % (host, nm[host].hostname()))
     print('State : %s' % nm[host].state())
     for proto in nm[host].all_protocols():
         print('----------')
         print('Protocol : %s' % proto)
 
         lport = nm[host][proto].keys()
         sorted(lport)
         for port in lport:
             print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

def save_csv_data(nm_csv):
    with open(filename+'.csv', 'w') as output:
        output.write(nm_csv)

if (len(sys.argv) > 1 and sys.argv[1]):
    save_csv_data(nm.csv(), path=sys.argv[1])
else:
    save_csv_data(nm.csv())

winsound.PlaySound('C:\Windows\media\tada.wav',1)


