# without classes

# mnemonic for stack methods
# 3PIES

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

n = int(input("Enter size of stack: "))
for i in range(n):
	element = input("Enter element " + str(i+1) + ": ")
	push(stack, element)

print("Popped Item:", pop(stack))
print("Stack after popping an element:", stack)