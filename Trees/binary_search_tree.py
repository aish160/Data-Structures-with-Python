class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data: # if the value already exists, don't add it
            # binary search trees dont support duplicate values
            return
        if data < self.data:
            # add this data in the left subtree
            if self.left: # not a leaf node
                self.left.add_child(data)
            else: # if left node is empty
                self.left = Node(data)
        else:
            # add this data in the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Node(data)
    
    # use in-order traversal to print the values
    # in-order: left -> root -> right
    def inorder_print(self):
        # this method will return a list of elements 
        # in your binary search tree in a specific order
        elements = []
        # visit the left subtree first
        if self.left:
            elements += self.left.inorder_print()

        # visit the root node
        elements.append(self.data)

        # visit the right subtree at last
        if self.right:
            elements += self.right.inorder_print()
        
        return elements
    
    def search(self, value):
        # Big-O of log n
        if self.data == value:
            return True
        if value < self.data:
            # value might be in the left subtree
            if self.left:
                return self.left.search(value)
            else:
                return False # this has reached an end

        if value > self.data:
            # value might be in the right subtree
            if self.right:
                return self.right.search(value)
            else:
                return False

def display_tree(elements):

    root = Node(elements[0]) # assume that the root node is the first element given as i/p

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    
    nodes = [17, 4, 1, 20, 9, 23, 18, 34]
    nodes_tree = display_tree(nodes)
    print("In-order Traversal:", nodes_tree.inorder_print())
    # the search function works even for strings, not just integers
    print("Does the search element exist in the given tree?", nodes_tree.search(13)) 


