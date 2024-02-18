from socket import *

PORT = 12345
s=socket(AF_INET, SOCK_DGRAM)
s.bind(("127.0.0.1",PORT))
while(1):
  m=s.recvfrom(PORT)
  print(m)

