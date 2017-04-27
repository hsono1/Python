class Bike(object):
	def __init__(self,price, max_speed):
		self.miles = 0
		self.price = price
		self.max_speed = max_speed

	def displayInfo(self):
		print self.price, self.max_speed, self.miles

	def ride(self):
		self.miles = self.miles + 10
		print 'Riding'
		return self

	def reverse(self):
		self.miles = self.miles - 5
		if self.miles < 0:
			self.miles = 0
		print 'Reversing'
		return self



bike1 = Bike(200,'25')
bike2 = Bike(500,'50')
bike3 = Bike(1200,'120')

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()


bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()


bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()





print ""
print ""
print ""


bike1.ride().ride().ride().reverse().displayInfo()

