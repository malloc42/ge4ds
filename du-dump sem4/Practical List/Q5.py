q = []

def enqueue():
    elt = int(input("Enter the element to be inserted: "))
    q.append(elt)
    print(elt, "is added to the queue")

def dequeue():
    if not q:
        print("Queue is empty")
    else:
        e = q.pop(0)
        print("Element dequeued is", e)
        print(q)

def display():
    print(q)

while True:
    print("Enter the operation:", "1. add", "2. remove", "3. display", "4. exit", sep="\n\t")
    ch = int(input())
    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("Please enter a valid operation")