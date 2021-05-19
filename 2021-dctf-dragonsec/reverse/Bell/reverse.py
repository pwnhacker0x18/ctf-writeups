from pwn import *

while True:
	c = remote("dctf-chall-bell.westeurope.azurecontainer.io", 5311)
	if c.recv().strip() == b'9':
		break
	c.close()

payload = "4140\n5017\n6097\n7432\n9089\n11155\n13744\n17007\n21147"

c.sendline(payload)
c.interactive()
