from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to receive ...")

while True:
     connectionSocket, addr = serverSocket.accept()

     #sentence = connectionSocket.recv(1024).decode()
     #print("s: ", sentence)

     #capitalizedSentence = sentence.upper()
     #connectionSocket.send(capitalizedSentence.encode())
     ####################################################
	# The server instructs the user to enter the information

     word1 = "Enter the amount from server: "
     connectionSocket.send(word1.encode())

	 # The server receives the information that the user types in and works on it as needed
     data1 = connectionSocket.recv(1024)
     amount = float(data1)

     print("received amount from server: ", amount)#print statement is for debugging purposes

# Same format here

     word2 = "Enter the number of years from server: "
     connectionSocket.send(word2.encode())

     data2 = connectionSocket.recv(1024).decode()
     years = int(data2)
     months = years * 12

     print("received months: ", months)#print statement is for debugging purposes

     word3 = "Enter the rate: "
     connectionSocket.send(word3.encode())

     data3  = connectionSocket.recv(1024).decode()
     rate10 = float(data3)

     #rate = rate10/100
     rate = rate10
     print("received rate: ", rate)

# The server does the final calculation to get the monthly payment

     #monthly_payment = amount * ((rate * ( 1 + rate)**months) / ((1 + rate)**(months - 1)))
     monthly_payment = amount * (rate *((1+rate)**months)) / (((1+rate)**(months))-1)
     print("monthly_payment", monthly_payment)#print statement is for debugging purposes

     connectionSocket.send(str(monthly_payment).encode())#monthly payments are sent to the user

     connectionSocket.close()
