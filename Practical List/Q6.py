class Node:
    def __init__(self, key):
        self.left = None
        self.value = key
        self.right = None

def insert(root, key):
    if root == None:
        return Node(key)
    if root.value == key:
        return root
    elif root.value < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def minValueNode(node):
    current = node
    while current.left != None:
        current = current.left
    return current

def delete(node, data):
    if not node:
        return None

    if data < node.value:
        node.left = delete(node.left, data)
    elif data > node.value:
        node.right = delete(node.right, data)
    else:
        # For node with only one child or no child
        if node.left != None:
            temp = node.right
            node = None
            return temp
        elif node.right != None:
            temp = node.left
            node = None
            return temp

        # For node with two children, get the in-order successor
        node.value = minValueNode(node.right).value
        node.right = delete(node.right, node.value)

    return node

def search(root, key):
    if root == None or root.value == key:
        return root
    if root.value < key:
        return search(root.right, key)
    else:
        return search(root.left, key)

def preOrderTraversal(node):
    if node is None:
        return
    print(node.value, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.value, end=", ")
    inOrderTraversal(node.right)

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.value, end=", ")

r = Node(15)
r = insert(r, 10)
r = insert(r, 18)
r = insert(r, 4)
r = insert(r, 11)
r = insert(r, 16)
r = insert(r, 20)
r = insert(r, 13)
print("Found" if search(r, 11) else "Not Found")
print("Found" if search(r, 80) else "Not Found")

x = 15
delete(r,x)

print("Preorder Traversal:", end=" ")
preOrderTraversal(r)
print("\nInorder Traversal:", end=" ")
inOrderTraversal(r)
print("\nPostorder Traversal:", end=" ")
postOrderTraversal(r)
