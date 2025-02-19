stack = []

def push(n):
	if len(stack) == n:
		print("The stack is full.")
	else:
		elt = input("Enter the element to be pushed: ")
		stack.append(elt)

def pop():
	if not stack:
		print("The stack is empty.")
	else:
		return stack.pop()

def display():
	for i in range(len(stack)-1, -1, -1):
		print(stack[i])

n = int(input("Enter the size of the stack: "))
while True:
	print("Select an operation:", "1. Push", "2. Pop", "3. Display", "4. Quit", sep="\n  ")
	c = int(input())
	if c == 1:
		push(n)
	elif c == 2:
		p = pop()
		if p != None:
			print("Popped element:", p)
	elif c == 3:
		display()
	elif c == 4:
		break
	else:
		print("Please enter a valid option.")