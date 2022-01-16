#การใช้ แบบ tuple เก็บค่าแบบคงที่
def demo_tuple():
	p11 = 'KANNATHAM', 'MEETHAMCHAI', 111
	print(p11)
	print('ชื่อ:',p11[0], p11[1]) # เรียกใช้ index 0
	print('ลำดับที่:', p11[-1])


 #การใช้ แบบ ดิกชันนารี
def demo_dit():
	p12 = {'fname':'Joe', 'lname':'Gomer', 'number':999}
	print(p12)
	print('ชื่อ', p12['fname'], p12['lname'], 'ลำดับ:', p12['number'])



#### การสร้าง class แบบที่1 #########
class Player:
	pass

def demo_player_class1():
	p11 = Player() 
	p11.fname = '4Q'
	p11.lname = 'Shop'
	p11.number = 11
	print(p11.fname, p11.lname, p11.number)#การใช้งาน
#-----------------

#### การสร้าง class แบบที่ 2 # เป็นวิธีทีเหมาะกว่าอันแรก
class Player2:
	def __init__(self):
		self.fname = ''
		self.lname = ''
		self.number = 22
def demo_player_class2():
	p22 = Player2()
	p22.fname = '4Q-2'
	p22.lname = 'Shop-2'
	p22.number = 22
	print(p22.fname, end='')
	print(p22.lname, end='')
	print(p22.number)
#-----------------


#### การสร้าง class แบบที่ 3 # code จะสั้นกว่าแบบ 1,2
class Player3:
	def __init__(self, fname, lname, number):
		self.fname = fname
		self.lname = lname
		self.number = number

def demo_player_class3():
	p33 = Player3('SADA', 'SHOP', 33)
	print(p33.fname)
	print(p33.lname)
	print(p33.number)
#-----------------


if __name__ == '__main__':
	# demo_tuple()
	# demo_dit()
	# demo_player_class1()
	# demo_player_class2()
	demo_player_class3()
