# more code below

''' class Node():
    
    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value
    
    def add_child(self, value):
# Compare the new value with the parent node
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.add_child(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.add_child(value)
        else:
            self.value = value
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()

root = Node(9)
root.add_child(1)
root.add_child(2)
root.add_child(3)

root.PrintTree() '''

class Node():
    
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, child, direction):
        if direction == "right":
            self.right = child
        elif direction == "left":
            self.left = child
    
    def findNode(self, parent):
        if parent.data < self.data:
            if self.left is None:
                return "Node not found"
            return self.left.findNode(self.left)
        elif parent.data > self.data:
            if self.right is None:
                return "Node not found"
            return self.right.findNode(self.right)
        else:
            return self
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
        
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
A.insert(B, "left")
B.insert(C, "right")
C.insert(D, "left")
A.insert(E, "right")
E.insert(F, "right")
A.printTree()