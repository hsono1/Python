class Animal(object):
	def __init__(self, animal_name):
		self.name = animal_name
		self.health = 100


	def walk(self):
		self.health = self.health - 1


	def run(self):
		self.health = self.health - 5

	def displayHealth(self):
		print "Animal's name  = {} \nAnimal's health = {}".format(self.name, self.health)



class Dog(Animal):
	def __init__(self, animal_name): 
		super(Dog, self).__init__(animal_name)
		self.health = 150

	def pet(self):
		self.health = self.health + 1


class Dragon(Animal):
	def __init__(self, animal_name): 
		super(Dragon, self).__init__(animal_name)
		self.health = 170

	def fly(self):
		self.health = self.health - 10
		
	def displayHealth(self):
		print "This is a Dragon"
		super(Dragon, self).displayHealth()


animal = Animal("animal")
animal.walk()
animal.walk()
animal.walk()
animal.run()
animal.run()
animal.displayHealth()

print ""
print ""

dog = Dog("bobby")
dog.walk()
dog.walk()
dog.walk()
dog.run()
dog.run()
dog.pet()
dog.displayHealth()


print ""
print ""

dragon = Dragon("dragonite")
dragon.walk()
dragon.walk()
dragon.walk()
dragon.run()
dragon.run()
dragon.fly()
dragon.fly()
dragon.displayHealth()







