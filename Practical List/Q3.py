class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, x):
        new = Node(x)
        if self.head == None:
            self.head = new
            new.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new
            new.next = self.head

    def remove(self, x):
        if self.head == None:
            return
        elif self.head.next == self.head:
            if self.head.data == x:
                self.head = None
        else:
            if self.head.data == x:
                old_head = self.head
                self.head = self.head.next
                current = old_head
                while current.next != old_head:
                    current = current.next
                current.next = self.head
            else:
                while True:
                    current = self.head
                    if current.next.data == x:
                        current.next = current.next.next
                        break
                    if current.next == self.head:
                        break
                    current = current.next

    def search(self, x):
        current = self.head
        if current == None:
            return
        else:
            while True:
                if current.data == x:
                    return current
                if current.next == self.head:
                    break
                current = current.next

    def traverse(self):
        current = self.head
        if current == None:
            return
        else:
            while True:
                print(current.data)
                if current.next == self.head:
                    break
                current = current.next

CL = CircularLinkedList()
while True:
    print("\n1. Insert an element",
          "2. Remove an element",
          "3. Search for an element",
          "4. Traverse the list",
          "5. Exit",
          sep="\n")
    c = int(input(">>> "))
    if c == 1:
        x = input("Enter an element to insert: ")
        CL.insert(x)
    elif c == 2:
        x = input("Enter an element to remove: ")
        CL.remove(x)
    elif c == 3:
        x = input("Enter an element to search: ")
        ptr = CL.search(x)
        if ptr == None:
            print("Element not found")
        else:
            print("Element found at node with pointer:", ptr)
    elif c == 4:
        CL.traverse()
    elif c == 5:
        break
    else:
        print("Please enter a valid operation.")
