from socket import *

#serverName = 'hostname'
#replace with the server-IP
#serverName = "10.11.2.2"
# use localhost if test on one machine

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#sentence = input("Input lowercase sentence: ")
#clientSocket.send(sentence.encode())

#modifiedSentence = clientSocket.recv(1024)

#print ("From Server:", modifiedSentence.decode())

#the word variable receives the instruction from the server, 
#the user types in the information and sends it to the server

word1 = clientSocket.recv(1024).decode()
amount = input(word1)

clientSocket.send(amount.encode())

word2 = clientSocket.recv(1024).decode()
years = input(word2)
clientSocket.send(years.encode())

word3 = clientSocket.recv(1024).decode()
rate = input(word3)
clientSocket.send(rate.encode())

#after the server calculates the monthly payment and sends it, 
# the client decodes the message and prints it for the user

monthly_payment = clientSocket.recv(1024).decode()
print("Monthly payment: ", monthly_payment)

clientSocket.close()
