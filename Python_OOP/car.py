class Car(object):
	def __init__(self, price,speed,fuel,mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 15
		else:
			self.tax = 12
		self.display_all()

	def display_all(self):
		print "price : {}, speed: {}, fuel = {}, mileage = {}, taxes = {}".format( self.price, self.speed, self.fuel, self.mileage, float(self.tax/100.0) )



car1 = Car(2000, 80, "full", 20)
car2 = Car(10000, 120, "full", 0)
car3 = Car(25000, 500, "empty", 180)
car4 = Car(100, 50, "half", 100)
car5 = Car(150000, 120, "full", 0)
car6 = Car(60000, 100, "half", 100)

