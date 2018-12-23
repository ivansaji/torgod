#! /usr/bin/python3
#A tor anonymizer to route all the traffic of the whole system through tor
# Works only for linux based systems

import os
import sys
import time

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

def torconnect():
	#code for tor connect

def tordisconnect():
	#code for tor disconnect

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
