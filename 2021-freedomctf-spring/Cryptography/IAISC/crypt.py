word = "&,!';!s#)q3v)xyqrsr0,xwu=)"
res = ''

for i in word:
	k = int(hex(ord(i)), 0) + 0x40
	if k > 128:
		res += chr(k-128)# + ' '
	else:
		res += chr(k)# + ' '

print(res)
