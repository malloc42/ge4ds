class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)

    def dequeue(self):
        return self.data.pop(0)

    def print_queue(self):
        print(self.data)

Q = Queue()
while True:
    print("\n1. Enqueue an element",
          "2. Dequeue an element",
          "3. Print the queue",
          "4. Exit",
          sep="\n")
    c = int(input(">>> "))
    if c == 1:
        x = input("Enter an element to enqueue: ")
        Q.enqueue(x)
    elif c == 2:
        if not Q.data:
            print("The queue is empty.")
        else:
            x = Q.dequeue()
            print("Element dequeued:", x)
    elif c == 3:
        Q.print_queue()
    elif c == 4:
        break
    else:
        print("Please select a valid operation.")
