class Player:
 
	def __init__(self):
		#super(Player, self).__init__()
		self.fname = ""
		self.lname = ""
		self.number = ""

class Player2:
	def __init__(self, fname, lname, number):
		self.fname = fname
		self.lname = lname
		self.number = number

if __name__ == '__main__':
	p1 = Player()
	p1.fname = "APPLE"
	p1.lname = "USA"
	p1.number = 1
	print(p1.fname, p1.lname, 'อันดับที่:', p1.number)

	p2 = Player2("KANNA", 'SADA', 555)
	print('ชื่อ:',p2.fname, '\nนามสกุล:', p2.lname, '\nหมายเลขประจำตัว:', p2.number)
	