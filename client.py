from socket import *

serverName = gethostname()
serverPort = 1234

clientSocket = socket(AF_INET, SOCK_DGRAM)
print(f"Connecting to server running on port {serverPort}")
message = "Hi from the client!"
clientSocket.sendto(message.encode(), (serverName, serverPort))
recvMessage, serverAddress = clientSocket.recvfrom(2048)

print(f"Message recived: {recvMessage}")
clientSocket.close()

