from base64 import decodestring
import hashlib

class vars:
	class boollst(object):
		def __init__(self):
			self.item = []
		def index(self,n):
			#print(n)
			#print(len(self.item))
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


class decode:
	def decode(string,binar):
		x = None
		for i in range(len(string)):
			x = str(format(ord(string[i]), "b"))
			while (len(x)<8):
				x = "0"+x
			for i in range(len(x)):
				#print(x[i] == "1")
				if (x[i] == "1"):
					binar.add(True)

				else:
					binar.add(False)
	def crypt(binar,keyar,binc):
		for i in range(len(binar.item)):
			if (binar.index(i) != keyar.index(i)):
				binc.add(True)
			else:
				binc.add(False)
	def encode(binar):
		c = 0;
		s = "";
		m = ""
		for i in range(len(binar.item)):
			c+=1
			if (binar.index(i)):
				s+="1"
			else:
				s+="0"
			if not (c<8):
				c = 0;
				#print(s)
				#print(len(s))
				m += (chr(int(s,2)))
				s = ""
		return m



			


