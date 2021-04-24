from pwn import *

def decrypt(data):
	byte = 0x0
	while byte < 0xff:
		j = xor(data, byte)
		k = j.find(b"CHTB{")
		log.info("Trying byte: " + hex(byte))
		if k != -1:
			log.success("flag index:" + str(k))
			log.success("key for decode xored data: " + hex(byte))
			break
		byte += 1
	return byte, k


def main():
	data = open("output.txt", 'r').readline()
	data = bytes.fromhex(data)
	log.success("Decrypter ;)")
	key, index = decrypt(data)
	data = xor(data, key)
	file = open('data', 'wb')
	file.write(data)
	file.close()
	log.success("Flag decrypted! Usage strings!")

if __name__ == '__main__':
	main()
