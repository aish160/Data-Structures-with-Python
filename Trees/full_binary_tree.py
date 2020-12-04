class Node:
    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None
    # Checking full binary tree
    def isFullTree(root):
        # Tree empty case
        if root is None:
            return True
        # Checking whether a child is present
        if root.leftChild is None and root.rightChild is None:
            return True
        if root.leftChild is not None and root.rightChild is not None:
            return (isFullTree(root.leftChild) and isFullTree(root.rightChild))
        return False
root = Node(1)
root.rightChild = Node(3)
root.leftChild = Node(2)
root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.rightChild.leftChild.leftChild = Node(6)
root.rightChild.leftChild.rightChild = Node(7)
if isFullTree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary full")