class Stack:
	def __init__(self):
		self.data = []

	def push(self, x):
		self.data.append(x)

	def is_empty(self):
		return self.data == []

	def pop(self):
		return self.data.pop()

	def top(self):
		return self.data[len(self.data)-1]

	def print_stack(self):
		for i in range(len(self.data)-1, -1, -1):
			print(self.data[i])

s = Stack()

while True:
	print("Select an operation:", "1. Push", "2. Pop", "3. Top", "4. Display", "5. Quit", sep="\n  ")
	c = int(input())

	if c == 1:
		x = input("Enter the element to be pushed: ")
		s.push(x)
	elif c == 2:
		if s.is_empty():
			print("The stack is empty.")
		else:
			print("Popped element:", s.pop())
	elif c == 3:
		if s.is_empty():
			print("The stack is empty.")
		else:
			print("The topmost element of the stack is", s.top())
	elif c == 4:
		if s.is_empty():
			print("The stack is empty.")
		else:
			s.print_stack()
	elif c == 5:
		break
	else:
		print("Please select a valid option.")