from socket import *

serverName = gethostname()
serverPort = 1234

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print(f"Server running on port {serverPort}")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(message.decode())
    clientMessage = f"Hi there {clientAddress}"
    serverSocket.sendto(clientMessage.encode(), clientAddress)