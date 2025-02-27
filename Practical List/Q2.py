class Node:
	def __init__(self, data):
		self.prev = None
		self.data = data
		self.next = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def insertbeg(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			return
		self.head.prev = new_node
		new_node.next = self.head
		self.head = new_node

	def insertend(self, data):
		new_node = Node(data)
		if not self.head:
			self.insertbeg(data)
		elif not self.head.next:
			new_node.prev = self.head
			self.head.next = new_node
		else:
			current_node = self.head
			while current_node:
				current_node = current_node.next
			new_node.prev = current_node
			current_node.next = new_node

	def traverse(self):
		current_node = self.head
		if not current_node:
			print("List is empty.")
			return
		while current_node:
			print(current_node.data)
			current_node = current_node.next

	def delbeg(self):
		if not self.head:
			print("List is empty.")
		elif not self.head.next:
			self.head = None
		else:
			self.head = self.head.next
			self.head.prev = None

	def delend(self):
		if not self.head:
			return
		elif not self.head.next:
			self.head = None
		else:
			current_node = self.head
			while current_node.next.next:
				current_node = current_node.next
			current_node.next = None

D1 = DoublyLinkedList()
while True:
	print("\nSelect an operation:",
		"1. Insert a node at the beginning.",
		"2. Insert a node at the end.",
		"3. Traverse through the linked list.",
		"4. Delete the first node.",
		"5. Delete the last node.",
		"6. Exit.", sep="\n  ")
	choice = int(input(">>> "))
	if choice == 1:
		num = int(input("Enter an integer element: "))
		D1.insertbeg(num)
	elif choice == 2:
		num = int(input("Enter an integer element: "))
		D1.insertend(num)
	elif choice == 3:
		D1.traverse()
	elif choice == 4:
		D1.delbeg()
	elif choice == 5:
		D1.delend()
	elif choice == 6:
		break
	else:
		print("Please enter a valid operation.")