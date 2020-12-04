""" 
EXERCISE
1. find_min(): finds minimum element in entire binary tree
minumum would be the left most element in the left subtree

2. find_max(): finds maximum element in entire binary tree
maximum would be the right most element in the right subtree

3. calculate_sum(): calcualtes sum of all elements

4. post_order_traversal(): performs post order traversal of a binary tree

5. pre_order_traversal(): perofrms pre order traversal of a binary tree
 """

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

    def postorder_print(self):
        # this method will return a list of elements 
        # in your binary search tree in a specific order
        elements = []
        # visit the left subtree first
        if self.left:
            elements += self.left.postorder_print()

        # visit the right subtree next
        if self.right:
            elements += self.right.postorder_print()

        # visit the root node at last
        elements.append(self.data)
        
        return elements

    def preorder_print(self):
        # this method will return a list of elements 
        # in your binary search tree in a specific order
        elements = []
        # visit the root node first
        elements.append(self.data)

        # then visit the left subtree
        if self.left:
            elements += self.left.preorder_print()

        # visit the right subtree at last
        if self.right:
            elements += self.right.preorder_print()
        
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

def sum_of_elements(elements):
    sum_ = sum(elements)
    return sum_

def find_min(elements):
    min_ = min(elements)
    return min_

def find_max(elements):
    max_ = max(elements)
    return max_

if __name__ == '__main__':
    
    nodes = [17, 4, 1, 20, 9, 23, 18, 34]
    nodes_tree = display_tree(nodes)
    print("In-order Traversal:", nodes_tree.inorder_print())
    print("Pre-order Traversal:", nodes_tree.preorder_print())
    print("Post-order Traversal:", nodes_tree.postorder_print())
    # the search function works even for strings, not just integers
    print("Does the search element exist in the given tree?", nodes_tree.search(13)) 
    print("Sum =", sum_of_elements(nodes))
    print("Minimum =", find_min(nodes))
    print("Maximum =", find_max(nodes))


