from socket import  *

s = socket ()

minhastr = "GET /rj/ HTTP/1.1\r\nHost: 10.10.13.1\r\nConnection: keep-alive\r\n\r\n"
print (minhastr)
meusbytes=str.encode (minhastr, "UTF-8")
print (meusbytes)

servidor="10.10.13.1"
porta=8752

s.connect((servidor, porta))
s.send (meusbytes)

data = s.recv (1024)

print (data)

s.close ()
