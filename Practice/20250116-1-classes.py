"""
Create a class Room that has data members 'length' and 'breadth'
and calculate the area of the room by creating a function calculate_area()
"""
class Room:
	length = 0
	# print(hex(id(length)))
	def __init__(self, length, breadth):
		# print(hex(id(length)))
		self.length = length # having same name seems to be a common practice
		self.breadth = breadth # the r.h.s. is referring to the formal parameter

	def calculate_area(self):
		print("Area of the room:", self.length*self.breadth, "sq. units")

# room1 = Room(1,1) # this cannot be left empty if __init__ was used

# classes need not have an initialiser
class NoInit:
	foo = 1001 # public by default
	bar = 1002

	def add_shiz(self):
		print("The sum is", self.foo+self.bar)

obj = NoInit()
print(obj.foo)

obj.add_shiz() # uses the default values

obj.foo = 29
obj.bar = 70
obj.add_shiz()
