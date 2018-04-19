import threading

total = 0
mutex = threading.Lock ()
def Hello (tid):
	global total
	print ("Sou a Thread "+str(tid))
	mutex.acquire ()
	aux = total
	aux+=tid
	total=aux
	mutex.release ()
threads=[]
for i in range (100):
	threads.append(threading.Thread(target=Hello, args=(i,)))
	threads[-1].start ()
for i in range (100):
	threads[i].join ()

print ("Acabei de criar as threads "+str(total))





















































































































