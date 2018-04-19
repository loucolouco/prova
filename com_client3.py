from socket import  *

s = socket ()

minhastr = "Mario João falaeeeee\r\n"
meusbytes=str.encode (minhastr, "UTF-8")


s.connect(("10.10.13.1", 8752))

while 1:
	meusbytes = raw_input("")
	s.send (meusbytes)
data = s.recv (1024)

print (data.decode("utf-8"))

s.close ()
