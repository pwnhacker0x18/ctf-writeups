data = "2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904"

data1 = bytes.fromhex(data)
file = open("data", "wb")
file.write(data1)
file.close()
print("decrypted and writed to 'data' filename!")
