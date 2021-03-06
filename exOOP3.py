# รู้จักกับ __init__() หรือ constructor

class Person:
	# constructor แบบ 1
	def __init__(self):
		self.fname = '' # ค่าเริ่มต้น ว่างๆ
		self.lname = ''
		self.contry = 'Thailand' # ค่าเริ่มต้น

class Person2:
	# constructor แบบ 2 กำหนดค่า None และใส่ค่าเริ่มต้นที่ต้องการ
	def __init__(self, fname=None, lname=None, contry='Thailand'):
		self.fname = fname
		self.lname = lname
		self.contry = contry

	#Overrides method object (โอเวอร์ไลเมตตอท)
	def __str__(self):
		return 'ชื่อ: {} นามสกุล: {} ประเทศ: {}'.format(self.fname, self.lname, self.contry)
#-----------


if __name__ == '__main__':
	# p1 = Person()
	# print(p1.fname)
	# print(p1.contry)

	p2 = Person2('ศักดิ์ดา','โชคดีมาก')
	print(p2)

