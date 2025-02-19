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
	print("\nPlease select an operation:",
		"1. Push",
		"2. Pop",
		"3. Top",
		"4. Display",
		"5. Exit", sep="\n  ")
	choice = int(input(">>> "))

	if choice == 1:
		n = int((input("Enter an integer to push: ")))
		s.push(n)
	elif choice == 2:
		if s.is_empty():
			print("The stack is empty.")
		else:
			p = s.pop()
			print("Popped Element:", p)
	elif choice == 3:
		if s.is_empty():
			print("The stack is empty.")
		else:
			t = s.top()
			print("Topmost Element:", t)
	elif choice == 4:
		s.print_stack()
	elif choice == 5:
		break
	else:
		print("Please select a valid operation.")