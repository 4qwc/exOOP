#exOOP4.py สร้างคลาสแล้วนำไป ใช้ import ใน demo_color.py
class Color:
	def __init__(self, color1, color2, color3):
		self.color1 = color1
		self.color2 = color2
		self.color3 = color3

	def Clr(self): # instance method
		return self.color1,  self.color2, self.color3


class Car:
	def __init__(self, toyota, honda, suzuki):
		self.toyota = toyota
		self.honda = honda
		self.suzuki = suzuki

	def Seri(self):
		return self.toyota, self.honda, self.suzuki



	 



 