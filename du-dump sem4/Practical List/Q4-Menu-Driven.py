def create():
	stack = []
	return stack

def push(stack, element):
	stack.append(element)
	return stack

def is_empty(stack):
	return len(stack) == 0

def pop(stack):
	if is_empty(stack):
		print("The stack is empty")
	else:
		return stack.pop()

def peek(stack):
	return stack[len(stack)-1]

def size(stack):
	return len(stack)

stack = create()

while True:
	print("Select an operation:", "1. View Stack", "2. Push an item",
		"3. Check if the stack is empty", "4. Pop", "5. Exit", sep="\n\t")
	c = int(input())
	if c == 1:
		print(stack)
	elif c == 2:
		item = input("Enter the item to push: ")
		push(stack, item)
		print(item, "pushed to stack")
	elif c == 3:
		if is_empty(stack):
			print("The stack is empty")
		else:
			print("The stack is not empty")
	elif c == 4:
		x = pop(stack)
		print("Popped item:", x)
	elif c == 5:
		break
	else:
		print("Enter a valid operation")