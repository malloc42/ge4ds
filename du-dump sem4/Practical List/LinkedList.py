class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insertbeg(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			return
		new_node.next = self.head
		self.head = new_node

	def insertend(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			return
		current_node = self.head
		while current_node.next:
			current_node = current_node.next
		current_node.next = new_node

	def insertindex(self, data, index):
		if index == 0:
			self.insertbeg(data)
			return
		pos = 0
		current_node = self.head
		while (current_node != None and pos+1 != index):
			pos += 1
			current_node = current_node.next
		if current_node:
			new_node = Node(data)
			new_node.next = current_node.next
			current_node.next = new_node
			return
		print("Invalid Index")

	def traverse(self):
		current_node = self.head
		while current_node:
			print(current_node.data)
			current_node = current_node.next

	def delfirst(self):
		if not self.head:
			return
		self.head = self.head.next

	def dellast(self):
		if self.head == None:
			self.delfirst()
			return
		current_node = self.head
		while (current_node.next != None and current_node.next.next != None):
			current_node = current_node.next
		current_node.next = None

L1 = LinkedList()
while True:
	print("\nSelect an operation:",
		"1. Insert a node at the beginning.",
		"2. Insert a node at the end.",
		"3. Insert a node at an index.",
		"4. Traverse through the linked list.",
		"5. Delete the first node.",
		"6. Delete the last node.",
		"7. Exit.", sep="\n  ")
	ch = int(input("Enter your choice: "))
	if ch == 1:
		num = int(input("Enter your data: "))
		L1.insertbeg(num)
	elif ch == 2:
		num = int(input("Enter your data: "))
		L1.insertend(num)
	elif ch == 3:
		num = int(input("Enter your data: "))
		index = int(input("Enter index (starts with 0): "))
		L1.insertindex(num, index)
	elif ch == 4:
		L1.traverse()
	elif ch == 5:
		L1.delfirst()
	elif ch == 6:
		L1.dellast()
	elif ch == 7:
		break
	else:
		print("Please enter a valid operation.")