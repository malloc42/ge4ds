class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, x):
        self.data.append(x)
    
    def pop(self):
        return self.data.pop()
    
    def top(self):
        return self.data[-1]
    
    def is_empty(self):
        return self.data == []
    
    def print_stack(self):
        for i in range(len(self.data)-1, -1, -1):
            print(self.data[i])

S = Stack()
while True:
    print("\n1. Push an element",
          "2. Pop an element",
          "3. Print the top element",
          "4. Print the stack",
          "5. Exit",
          sep="\n")
    c = int(input(">>> "))
    if c == 1:
        n = input("Enter an element to push: ")
        S.push(n)
    elif c == 2:
        if S.is_empty():
            print("The stack is empty.")
        else:
            p = S.pop()
            print("Popped Element:", p)
    elif c == 3:
        if S.is_empty():
            print("The stack is empty.")
        else:
            t = S.top()
            print("Topmost Element:", t)
    elif c == 4:
        S.print_stack()
    elif c == 5:
        break
    else:
        print("Please select a valid operation.")

operators = ["+", "-", "*", "/", "^"]
operands = Stack()

expr = input("Enter the postfix expression: ").split()
for x in expr:
    if x not in operators:
        operands.push(x)
    else:
        b = eval(operands.pop())
        a = eval(operands.pop())
        if x == "+":
            ans = a+b
        elif x == "-":
            ans = a-b
        elif x == "*":
            ans = a*b
        elif x == "/":
            ans = a/b
        elif x == "^":
            ans = a**b
        operands.push(str(ans))

print("The given postfix expression evaluates to:", operands.top())
