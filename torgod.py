#! /usr/bin/python3
#A tor anonymizer to route all the traffic of the whole system through tor
# Works only for linux based systems

import os

def logo():
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

def main():
	clearscreen()
	logo()
	print('Tor anonymizer')
	opt1=input('\n Choose an option \n\n 1)	Connect to Tor\n 2)	Disconnect From Tor \n')

main()
