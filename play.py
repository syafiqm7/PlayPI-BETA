from getpass import getpass
import os
import sys
import random
import time 
import socket
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#print('Please enter your name ')
#name = input("----> ")

#def GetUc():
	#option = input('Please enter your password : ')
        #if option == 's3cr3t':
		#Main()
	#else:
		#print('Wrong password !')
		#time.sleep(5)
		#pass
		
def Main():
	os.system('clear')
	os.system('figlet playPI BETA | lolcat')
	print('      \033[1;92mcreated by Syafiq'.format(minute, hour, day, year))
	print(" ")
	print(" ")
	print('Welcome ')
	print('[ 1 ] Starwar ')
	print('[ 2 ] Eliza ')
	print('[ 3 ] Moon - Buggy ')
	print('[ 4 ] Map ')
	print('[ 5 ] Fire ')
	print('[ 6 ] Guess the number (UNDER CONSTRUCTION)')
	print('[ 7 ] Haculator ')
	print('[ 8 ] Matrix Rainfall ')
	print('[ 9 ] CHAT me ')
	print('[ 10 ] quit ')
	option = input('Please enter the number : ')
	if option == '1':
		os.system('echo please type starwars | lolcat')
		os.system('telnet telehack.com')
		os.system('starwars ')
	elif option == '2':
		os.system('echo please type eliza | lolcat')
		os.system('telnet telehack.com')
		os.system('eliza')
	elif option == '3':
		os.system('clear')
		os.system('moon-buggy | lolcat ')
	elif option == '4':
		os.system('clear')
		os.system('telnet mapscii.me')
	elif option == '5':
		os.system('cacafire')
	elif option == '6':
		os.system('echo Sorry , this game is under construction . | lolcat')
	elif option == '7':
		Menu()
	elif option == '8':
		os.system('cmatrix')
	elif option == '9':
		os.system('clear')
		ChatMe()
	elif option == '10':
		os.system('echo created by syafiq | lolcat')
		os.system('echo Bye ^_^ | lolcat')
	else:
		Main()
		
def Menu():
	os.system('cowsay HACulator | lolcat ')
	os.system('echo created by : Syafiq | lolcat')
	os.system('echo Your best companion ! | lolcat')
	Hakulator()

ical = " " 

def Hakulator():
      if "1" == ical:
       print("Options:")
      print("Enter 'add' to add two numbers")
      print("Enter 'subtract' to subtract two numbers")
      print("Enter 'multiply' to multiply two numbers")
      print("Enter 'divide' to divide two numbers")
      print("Enter 'quit' to end the program")
      
      user_input = input(" : ")

      if user_input == "quit": 
        return 
      elif user_input == "add" :
         num1 = float(input("Number:"))
         num2 = float(input("Number:"))
         result  = num1 + num2
         print("The answer is " + str (result ))
         return (input(Hakulator()))
      elif user_input == "subtract":
         num1 = float(input("Number:"))
         num2 = float(input("Number:"))
         result = num1 - num2
         print("The answer is " + str (result ))  
         return (input(Hakulator())) 
      elif user_input == "multiply":
         num1 = float(input("Number:"))
         num2 = float(input("Number:"))
         result  = num1 * num2
         print("The answer is " + str (result ))
         return (input(Hakulator()))
      elif user_input == "divide":
         num1 = float(input("Number:"))
         num2 = float(input("Number:"))
         result  = num1 / num2
         print("The answer is " + str (result ))
         return (input(Hakulator()))
      else:
         print("Unknown input")
         return (input(Hakulator()))
         
def ChatMe():
	os.system('figlet CHAT me | lolcat')
	os.system('echo Created by : Syafiq | lolcat')
	print('Please chose :')
	print('[ 1 ] Server ')
	print('[ 2 ] Client ')
	print('[ 3 ] How to use Chat Me ')
	option = input('---> ')
	if option == '1':
		Server()
	elif option == '2':
		Client()
	elif option == '3':
		print('1)If you choose server , please send the hostname to your friend')
		print('2)Make sure he/she choose client and ask him to put the hostname')
		print('3)Server have to start the conversation')
		print('4)Enjoy!!')
		print('Caution, never send blank message to your friend or it will crash!')
		ChatMe()
	else:
		Main()
         
def Client():
	s = socket.socket()
	host = input(str('Please enter the hostname :'))
	print('Please ask your friend to send the hostname ')
	port = 8080
	s.connect ( (host,port) )
	print('Connected to the server ')
	print(" ")
	while 1:
		incoming_message = s.recv(1024)
		incoming_message = incoming_message.decode( )
		print('Typing....')
		print(' ')
		time.sleep(2)
		print('HOST : ' , incoming_message)
		print(" ")
		message = input(str('---> '))
		message = message.encode( )
		s.send(message)
		print('message has been sent ')
		print(" ")
	
def Server():
	s = socket.socket( )
	host = socket.gethostname( )
	print('Server name : ' , host)
	print('Sent this to your friend ( server )')
	port = 8080
	s.bind( ( host , port ) )
	print(" ")
	print('Server done binding to host and port ')
	print(" ")
	print("Server is waiting for incoming connection ....")
	print(" ")
	s.listen(1)
	conn, addr = s.accept( )
	print(addr , 'Has connected to the server ')
	print(" ")
	while 1:
		message = input(str("----> "))
		message = message.encode( )
		conn.send(message)
		print("Message has been sent")
		print(" ")
		incoming_message = conn.recv(1024)
		incoming_message = incoming_message.decode( )
		print('Typing...')
		print(' ')
		time.sleep(2)
		print('CLIENT : ' , incoming_message)
		print(" ")
	
Main()
