#! /usr/bin/python3
#A tor anonymizer to route all the traffic of the whole system through tor
# Works only for linux based systems

import os
import sys
import time
from commands import getoutput

def logo():
	clearscreen()
	x='''                                                                                                                        
                                                                                                                
			TTTTTTTTTTTTTTTTTTTTTTT                                               GGGGGGGGGGGGG                             d::::::d
			T:::::::::::::::::::::T                                            GGG::::::::::::G                             d::::::d
			T:::::::::::::::::::::T                                          GG:::::::::::::::G                             d::::::d
			T:::::TT:::::::TT:::::T                                         G:::::GGGGGGGG::::G                             d:::::d 
			TTTTTT  T:::::T  TTTTTTooooooooooo   rrrrr   rrrrrrrrr         G:::::G       GGGGGG   ooooooooooo       ddddddddd:::::d 
			        T:::::T      oo:::::::::::oo r::::rrr:::::::::r       G:::::G               oo:::::::::::oo   dd::::::::::::::d 
			        T:::::T     o:::::::::::::::or:::::::::::::::::r      G:::::G              o:::::::::::::::o d::::::::::::::::d 
			        T:::::T     o:::::ooooo:::::orr::::::rrrrr::::::r     G:::::G    GGGGGGGGGGo:::::ooooo:::::od:::::::ddddd:::::d 
			        T:::::T     o::::o     o::::o r:::::r     r:::::r     G:::::G    G::::::::Go::::o     o::::od::::::d    d:::::d 
			        T:::::T     o::::o     o::::o r:::::r     rrrrrrr     G:::::G    GGGGG::::Go::::o     o::::od:::::d     d:::::d 
			        T:::::T     o::::o     o::::o r:::::r                 G:::::G        G::::Go::::o     o::::od:::::d     d:::::d 
			        T:::::T     o::::o     o::::o r:::::r                  G:::::G       G::::Go::::o     o::::od:::::d     d:::::d 
			      TT:::::::TT   o:::::ooooo:::::o r:::::r                   G:::::GGGGGGGG::::Go:::::ooooo:::::od::::::ddddd::::::dd
			      T:::::::::T   o:::::::::::::::o r:::::r                    GG:::::::::::::::Go:::::::::::::::o d:::::::::::::::::d
			      T:::::::::T    oo:::::::::::oo  r:::::r                      GGG::::::GGG:::G oo:::::::::::oo   d:::::::::ddd::::d
			      TTTTTTTTTTT      ooooooooooo    rrrrrrr                         GGGGGG   GGGG   ooooooooooo      ddddddddd   ddddd
			                                                                                                                        
			        Created By : CyberFreak                                                                                                               
			                                                                                                                        
			                                                                                                                        
			                                                                                                                        
			                                                                                                                        
			                                                                                                                        '''
	print(x)

def clearscreen():
	os.system('clear');

def exitfn():
	exit(0)

TorrcCfgString = """

##/////ADDED BY ToRGOD ///
VirtualAddrNetwork 10.0.0.0/10
AutomapHostsOnResolve 1
TransPort 9040
DNSPort 53
ControlPort 9051


"""

resolvString = "nameserver 127.0.0.1"

Torrc = "/etc/tor/torrc"
resolv = "/etc/resolv.conf"



def torconnect():
	#code for tor connect
	if TorrcCfgString in open(Torrc).read():
		print("\nTor Setting configured already")
	
	else:
		with open(Torrc,"a") as myfile:
			myfile.write(TorrcCfgString)
			print('\nTor settings configured')

	if resolvString in open(resolv).read():
		print("\nDNS Setting configured already")
	
	else:
		with open(resolv,"w") as myfile:
			myfile.write(TorrcCfgString)
			print('\nDNS settings configured')


	print("\nStarting TOR SERVICE")
	os.system("\nservice tor start")
	print("\nsetting Up IPTABLES")
	
	iptables_rules = """
	NON_TOR="192.168.1.0/24 192.168.0.0/24"
	TOR_UID=%s
	TRANS_PORT="9040"

	iptables -F
	iptables -t nat -F

	iptables -t nat -A OUTPUT -m owner --uid-owner $TOR_UID -j RETURN
	iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports 53
	for NET in $NON_TOR 127.0.0.0/9 127.128.0.0/10; do
	 iptables -t nat -A OUTPUT -d $NET -j RETURN
	done
	iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports $TRANS_PORT

	iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
	for NET in $NON_TOR 127.0.0.0/8; do
	 iptables -A OUTPUT -d $NET -j ACCEPT
	done
	iptables -A OUTPUT -m owner --uid-owner $TOR_UID -j ACCEPT
	iptables -A OUTPUT -j REJECT
	"""%(getoutput("id -ur debian-tor"))

	os.system(iptables_rules)
	print("\nSetUp IPTABLES")
	print t()+" \nFetching current IP..."
	print t()+" \nCURRENT IP : "+ip()
	

def tordisconnect():
	#code for tor disconnect
	print('\nStopping torghost')
	print(t()+"Reseting IPTABLES")
	IpFlush = """
	iptables -P INPUT ACCEPT
	iptables -P FORWARD ACCEPT
	iptables -P OUTPUT ACCEPT
	iptables -t nat -F
	iptables -t mangle -F
	iptables -F
	iptables -X
	"""
	os.system(IpFlush)

	print("Done setting up IPTABLES")
	print(t()+"restarting network manager")
	os.system("service network-manager restart")
	print("\n restart network-manager restart")
	print('\nFetching IP')
	print(t()+"The Ip is"+ip())


def t():
	current_time=time.localtime()
	ctime = time.strftime('%H:%M:%S', current_time)
	return "["+ ctime + "]"

def ip():
	while True:
		try:
			ipadd = commands.getstatusoutput('wget -qO- https://check.torproject.org | grep -Po "(?<=strong>)[\d\.]+(?=</strong)"')
		except :
			continue
		break
	return ipadd[1]


def main():
	clearscreen()
	logo()
	print('Tor anonymizer')
	opt1=input('\n Choose an option \n\n 1)	Connect to Tor\n 2)	Disconnect From Tor \n	3)	Exit')
	if opt1=='1':
		clearscreen()
		torconnect()

	elif opt1=='2':
		clearscreen()
		tordisconnect()

	elif opt1=='3':
		clearscreen()
		exitfn()

	else

main()
