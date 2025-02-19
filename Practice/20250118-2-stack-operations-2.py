# attempt
# with class
class Stack:
	def __init__(self):
		self.stack = []

	def push(self, x):
		self.stack.append(x)

	def is_empty(self):
		return len(self.stack) == 0

	def pop(self):
		if self.is_empty():
			print("The stack is empty")
		else:
			return self.stack.pop()

	def peek(self):
		return self.stack[len(self.stack)-1]

	def size(self):
		return len(self.stack)

my_stack = Stack()

n = int(input("Enter size of stack: "))
for i in range(n):
	element = input("Enter element " + str(i+1) + ": ")
	my_stack.push(element)

print("Popped Element:", my_stack.pop())
print("Stack after popping an element:", my_stack.stack)