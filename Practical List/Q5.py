class Queue:
	def __init__(self):
		self.data = []

	def enqueue(self, elt):
		self.data.append(elt)

	def dequeue(self):
		return self.data.pop(0)

	def display(self):
		print(self.data)

q = Queue()

while True:
	print("\nPlease select an operation:",
		"1. Enqueue",
		"2. Dequeue",
		"3. Display",
		"4. Exit", sep="\n  ")
	choice = int(input(">>> "))

	if choice == 1:
		x = int(input("Enter an integer to enqueue: "))
		q.enqueue(x)
	elif choice == 2:
		if not q.data:
			print("The queue is empty.")
		else:
			x = q.dequeue()
			print("Element dequeued:", x)
	elif choice == 3:
		q.display()
	elif choice == 4:
		break
	else:
		print("Please select a valid operation.")