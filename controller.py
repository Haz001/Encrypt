from function import *
while True:
	_bin = vars.boollst()
	_key = vars.boollst()
	_bin2 = vars.boollst()
	decode.decode(input("Message:\n"),_bin)
	keytext = input("Password:\n").encode()
	keyhash = hashlib.sha512(keytext).hexdigest()
	decode.decode(keyhash,_key)
	print("Key length: "+str(len(_key.item)))
	decode.crypt(_bin,_key,_bin2)
	print("Encripted Text:\n"+decode.encode(_bin2))

	input()
