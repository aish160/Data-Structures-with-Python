class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def add_child(self, child, direction):
        if direction == "L":
            self.left = child 
        elif direction == "R":
            self.right = child
        else:
            print("Invalid Direction")
    
    def printTree(self, traversal):
        if traversal == 1: #preorder
            print(self.data)
            if self.left:
                self.left.printTree(1)
            if self.right:
                self.right.printTree(1)
        elif traversal == 2: #inorder
            if self.left:
                self.left.printTree(2)
            print(self.data)
            if self.right:
                self.right.printTree(2)
        elif traversal == 3: #postorder
            if self.left:
                self.left.printTree(3)
            if self.right:
                self.right.printTree(3)
            print(self.data)
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
A.add_child(B, "L")
B.add_child(D, "L")
B.add_child(E, "R")
A.add_child(C, "R")
C.add_child(F, "L")
C.add_child(G, "R")
A.printTree(2)