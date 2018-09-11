from base64 import decodestring

class vars:
	class boollst(object):
		def __init__(self):
			self.item = []
		def index(self,n):
			print(n)
			print(len(self.item))
			if (n < len(self.item)):
				return self.item[n]
			else:
				return None
			
		def add(self,b):
			try:
				self.item.append(b)
				return True
			except:
				return False


_bin = vars.boollst()
_bin2 = vars.boollst()
x = 0
while x < 5:
	_bin.add(True)
	x+=1
print(_bin2.item)
print(_bin.item)

class decode:
	def base64bin(string):
		x = None
		for i in range(len(string)):
			x = format(ord(string[i]), "b")
			if (x == 0):
				_bin.add(True)
			else:
				_bin.add(True)
