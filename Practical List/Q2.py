class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beg(self, x):
        new = Node(x)
        if not self.head:
            self.head = new
        else:
            self.head.prev = new
            new.next = self.head
            self.head = new

    def insert_end(self, x):
        new = Node(x)
        if not self.head:
            self.insert_beg(x)
        elif not self.head.next:
            new.prev = self.head
            self.head.next = new
        else:
            current = self.head
            while current.next:
                current = current.next
            new.prev = current
            current.next = new

    def del_beg(self):
        if not self.head:
            print("List is empty.")
        elif not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def del_end(self):
        if not self.head:
            return
        elif not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

    def traverse(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data)
            current = current.next

DL = DoublyLinkedList()
while True:
    print("\n1. Insert at the beginning",
          "2. Insert at the end",
          "3. Remove from the beginnning",
          "4. Remove from the end",
          "5. Traverse the list",
          "6. Exit",
          sep="\n")
    c = int(input(">>> "))
    if c == 1:
        x = input("Enter an element to insert: ")
        DL.insert_beg(x)
    elif c == 2:
        x = input("Enter an element to insert: ")
        DL.insert_end(x)
    elif c == 3:
        DL.del_beg()
    elif c == 4:
        DL.del_end()
    elif c == 5:
        DL.traverse()
    elif c == 6:
        break
    else:
        print("Please enter a valid operation.")
