class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beg(self, x):
        new = Node(x)
        if self.head == None:
            self.head = new
        else:
            new.next = self.head
            self.head = new

    def insert_index(self, x, i):
        if i == 1:
            self.insert_beg(x)
        else:
            pos = 1
            current = self.head
            while current != None and pos+1 != i:
                pos += 1
                current = current.next
            if current != None:
                new = Node(x)
                new.next = current.next
                current.next = new
            else:
                print("Invalid index.")

    def insert_end(self, x):
        new = Node(x)
        if self.head == None:
            self.head = new
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new

    def del_beg(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next

    def del_index(self, i):
        if self.head == None:
            return
        elif i == 1:
            self.del_beg()
        else:
            pos = 1
            current = self.head
            while current != None and pos+1 != i:
                pos += 1
                current = current.next
            if current != None and current.next != None:
                current.next = current.next.next
            else:
                print("Invalid index.")

    def del_end(self):
        if self.head == None:
            return
        elif self.head.next == None:
            self.head = None
        else:
            current = self.head
            while current.next != None and current.next.next != None:
                current = current.next
            current.next = None

    def traverse(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def search(self, x):
        current = self.head
        while current != None:
            if current.data == x:
                return current
            current = current.next

L = SinglyLinkedList()
while True:
    print("\n1. Insert at the beginning",
          "2. Insert at a position",
          "3. Insert at the end",
          "4. Remove from the beginning",
          "5. Remove from a position",
          "6. Remove from the end",
          "7. Traverse the list",
          "8. Search for an element",
          "9. Exit",
          sep="\n")
    c = int(input(">>> "))
    if c == 1:
        x = input("Enter the element to insert: ")
        L.insert_beg(x)
    elif c == 2:
        x = input("Enter the element to insert: ")
        i = int(input("Enter the position (starts from 1): "))
        L.insert_index(x, i)
    elif c == 3:
        x = input("Enter the element to insert: ")
        L.insert_end(x)
    elif c == 4:
        L.del_beg()
    elif c == 5:
        i = int(input("Enter the position (starts from 1): "))
        L.del_index(i)
    elif c == 6:
        L.del_end()
    elif c == 7:
        L.traverse()
    elif c == 8:
        x = input("Enter the element to search: ")
        ptr = L.search(x)
        if ptr == None:
            print("Element not found.")
        else:
            print("Element found at node with pointer:", ptr)
    elif c == 9:
        break
    else:
        print("Please enter a valid option.")
