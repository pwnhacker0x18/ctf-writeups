from pwn import *

c = remote("138.68.147.93", 31256)

c.sendline("1")
c.recvuntil("Here is a little help:\n\n")
data = c.recv().decode()
data = data.split(" \n\n1. ❓")
data = data[0]
data = data.replace("-> ", '')
data = data.split()

c.sendline("2")
i = 1
while i <= 500:
	c.recvuntil(":\n\n")
	data1 = c.recv().decode()
	data1 = data1.split(" = ?")
	data1 = data1[0]
#	print(data)
#	print(data1)

	j = 0
	data2 = data1.replace(data[0], data[(1)])
	while j < 18:
		j += 2
		data2 = data2.replace(data[j], data[(j+1)])



	res = str(eval(data2))
	c.sendline(res)
	log.info("Answer %d sent" % i)
	i += 1

log.info("GET FLAG!!!")
c.interactive()
