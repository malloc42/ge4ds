q = []

def enqueue(elt):
	q.append(elt)

def dequeue():
	if not q:
		print("The queue is empty.")
	else:
		e = q.pop(0)
		return e

def display():
	print(q)


while True:
	print("Select an operation:", "1. Enqueue", "2. Dequeue", "3. Display", "4. Quit", sep="\n  ")
	c = int(input())

	if c == 1:
		elt = input("Enter the element to enqueued: ")
		enqueue(elt)
	elif c == 2:
		dq_elt = dequeue()
		if dq_elt != None:
			print("Element dequeued is", dq_elt)
	elif c == 3:
		display()
	elif c == 4:
		break
	else:
		print("Please enter a valid option.")