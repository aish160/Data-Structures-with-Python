# Representing a Tree using Lists : List of Lists
def BinaryTree(r):
    return [r, [], []]
    # if you want to insert a child node on the left, 
    # you need to insert it in the second position, i.e, index position 1.
def insertLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1: # if it's not empty
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)

# insert left child elements
insertLeft(r, 4)
insertLeft(r, 5)

# insert right child elements
insertRight(r, 6)
insertRight(r, 7)

left = getLeftChild(r)  # prints the left node of the root node
print("Left Child Node:",left)

right = getRightChild(r)  # prints the right node of the root node
print("Right Child Node:",right)

setRootVal(left, 9)  # sets the root value of the left node to 9
print(r)

'''
OUTPUT:
Left Child Node: [5, [4, [], []], []]
Right Child Node: [7, [], [6, [], []]]
[3, [9, [4, [], []], []], [7, [], [6, [], []]]]
'''