class Person:
	# attr without using __init__
	foo = 1001 # this will be made public by default

	def __init__(self, name, age, passkey): # obj attr initialiser
		self.NAME = name # object will have attribute AGE
		self.AGE = age
		self.__PASSKEY = passkey # leading __ creates a private attribute

	def greet(self): # all class methods will at least have the self parameter
		print("Hello", self.NAME + "!")
		print("You are", self.AGE, "years old.")
		# if self. is not used, it can cause problems when the attr name is different
		# eg. NAME and name 

# creating class variables
p1 = Person("Alice", 19, "saymyname")
p2 = Person("Bob", 18, "heisenberg")

# using class methods
p1.greet()
p2.greet()

# accessing object attrs
print(p1.NAME)
print(p2.AGE)
print(p1.foo)
# print(p1.__PASSKEY) # error, the attribute is private

# not discussed
# we can create 'getters' to access private attrs
# and 'setters' to modify them

# modifying object attrs
p1.NAME = "Alaina"
p1.greet()