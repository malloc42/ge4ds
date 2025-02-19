class Stack:
	def __init__(self):
		self.data = []
	def push(self, x):
		self.data.append(x)
	def pop(self):
		return self.data.pop()
	def top(self):
		return self.data[-1]
	def is_empty(self):
		return self.data == []
	def print_stack(self):
		for i in range(len(self.data)-1, -1, -1):
			print(self.data[i])

s = Stack()
while True:
	print("Select an operation",
		"1. Push",
		"2. Pop",
		"3. Top",
		"4. Display",
		"5. Exit", sep="\n  ")
	c = int(input())
	if c == 1:
		n = int((input("Enter an integer element: ")))
		s.push(n)
	elif c == 2:
		if s.is_empty():
			print("The stack is empty.")
		else:
			p = s.pop()
			print("Popped Element:", p)
	elif c == 3:
		if s.is_empty():
			print("The stack is empty.")
		else:
			t = s.top()
			print("Topmost Element:", t)
	elif c == 4:
		s.print_stack()
	elif c == 5:
		break
	else:
		print("Please select a valid operation.")