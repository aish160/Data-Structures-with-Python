# **Tree Data Structures** <br>
A tree DS has a root, branches, and leaves. All the children of one node are independent of of the children of another node. Each leaf node is unique. In a file system, directories or folders are structured as trees.

Trees are non-linear data structures. A non-linear data structure has multiple layers, in a hierarchical order. Trees are unidirectional (top to bottom).

### **Terminology:**<br>
1. Node: It is a fundamental part of a tree. Nodes store information. 
2. Edge: An edge connects two nodes to show that there is a relation between them. Every node is connected by exactly one incoming edge from another node, except the root node which has none. But each node may have sevearl outgoing edges.
3. Root: It is the only node in the tree that has no incoming edges. It has no parent node.
4. Path: A path is an ordered list of nodes that are connected by edges. It's a sequence of consecutive edges from source node to the destination node. 
5. Children: The node below a given node connected by its edges downwards is called its child node. These have incoming edges, and maybe outgoing edges.
6. Siblings: Children of the same parent node are said to be siblings.
7. Subtree: A set of nodes and edges comprised of a parent node and all descendants of that parent is called a subtree.
8. Leaf Node: Leaf node is a node that has no children. These are also called external nodes.
9. Non-Leaf Node: Non-Leaf nodes have at least one child node. These are also called internal nodes.
10. Traversing: Passing through nodes in a sequential order is called traversing the tree.
11. Ancestor: Any predecessor node on the path from root node to that particular node is called the ancestor node to that node.
12. Descendant: Any successor node on the path from that particular node to the leaf node is called the descendant node to that node.
13. Degree: Degree of a node is the number of children to that node. Degree of a tree is the maximum degree among all nodes.
14. Depth: Depth of a node is the length of path from root to that node. Depth of root node is always 0.
15. Height: Height of a node is the number of edges in the longest path from that node to a leaf. Height is the opposite of depth. The height and depth of a node may or may not be same.<br>
    ```Height of a tree = Height of its root node.```
16. Level: The number of edges from root to the given node is called level.<br>
    ```Level of the tree = Height of the tree```<br>
    ```Level of a node ≠ Height of a node```<br>
    ```Level of a tree = Depth of a node```<br>

**Representation of a tree in linked lists:** (Fig.1)

[IMAGE HERE](https://www.studytonight.com/data-structures/images/introduction-to-binary-trees-1.png)

### **Important points to note:**
1. If a tree has n nodes, there will be (n-1) edges.
2. Trees are acyclic.
3. Applications of trees:<br>
    1. Store hierarchical data, like folder structure, organizational structre, XML/HTML data.
    2. Binary search trees allow fast search, insertion, deletion on sorted data. They also help find the closest item to a given item.
    3. Heap is a tree DS which is implemented using arrays and used to implement priority queues.
4. Trees are recursive data structures where a child node is another tree on itself.

## **Binary Trees:**
A binary tree is a tree in which each node can have atmost 2 children (so, it can have 0, or 1, or 2 children).

### **Properties of a binary tree:**
1. At level 0 in a binary tree, the maximum nodes possible are 1. At level 1, the maximum nodes possible are 2. At level 2, 4 are possible. So, the maximum number of nodes present in level (i) = 2^i.
2. Maximum number of nodes present at height (h) = 2^(h+1)-1
3. Minimum number of nodes present at height (h) = h+1
4. Maximum height with n nodes, h = n-1
5. Minimum height with n nodes, h = log(n+1)1

### **Types of Binary Trees:**
1. Full or, Proper or, Strict Binary Tree
2. Complete Binary Tree
3. Perfect Binary Tree
4. Degenerate Binary Tree

#### **Full Binary Tree:** 
Each node has either 0 or 2 child nodes. A full binary tree is a binary tree in which all nodes except leaf nodes have 2 children.
In a full binary tree, number of lead nodes is one greater than the number of internal nodes. So, if l is the number of leaf nodes and i is the number of internal nodes, l = i+1

**Properties of a full binary tree:**
1. Maximum number of nodes with height (h), n = 2^(h+1)-1 (this is the same as the maximum nodes for a basic binary tree 0).
2. Minimum number of nodes whith height (h), n = 2h+1
3. Minimum height, h = log(n+1)-1
4. Maximum height, h = (n-1)/2 where n is the number of nodes.

#### **Complete Binary Tree:**
A binary tree is a complete binary tree if all the levels arae completely filled except possibly the last level and the last level has all nodes as *left* as possible.
Tip: Fill the nodes from left to right. Only if all the left positions are complete/occupied, go right.

***All full binary trees are complete binary trees, but not all complete binary trees are full.***

**Properties of complete binary trees:**
1. Maximum nodes of height (h) = 2^(h+1)-1
2. Minimum nodes of height (h) = 2^h
3. Minimum height = log(n+1)-1
4. Maximum height = log(n)

#### **Perfect Binary Tree:**
If all internal nodes have 2 child nodes each and all leaves are at the same level, then the binary tree is called a perfect binary tree.
 
***Every perfect binary tree can be a full and a complete binary tree. But the other way isn't true.***

#### **Degenerate Binary Tree:**
A binary tree in which all internal nodes have one child each is called a degenerate tree. It could be either left-skewed binary tree or a right-skewed binary tree.

## **Binary Tree Traversals**
1. Pre-order
2. In-order
3. Post-order

Consider the following binary tree: (Fig.2)
[IMAGE HERE](https://github.com/srinijadharani/Data-Structures-and-Algorithms-with-Python/blob/main/Trees/traversal.png)
### **Pre-order Traversal:**
**Traversal Order**: Root -> Left -> Right
1. Check if the current node is empty/null.
2. Display the data part of the root or the current node.
3. Traversethe left subtree by recursiverly calling the pre-order function.
4. Traverse the right subtree by recursively calling the pre-order function.

**Pre-order traversal for Fig.2:** A B D E G H C F I

### **In-order Traversal:**
**Traversal Order**: Left -> Root -> Right
1. Check if the current node is empty/null.
2. Traversethe left subtree by recursiverly calling the pre-order function.
3. Display the data part of the root or the current node. 
4. Traverse the right subtree by recursively calling the pre-order function.

**Pre-order traversal for Fig.2:** D B G E H A C F I

### **Post-order Traversal:**
**Traversal Order**: Left -> Right -> Root
1. Check if the current node is empty/null.
2. Traversethe left subtree by recursiverly calling the pre-order function.
3. Traverse the right subtree by recursively calling the pre-order function.
4. Display the data part of the root or the current node. 

**Pre-order traversal for Fig.2:** D G H B E I F C A

### **AVL Trees:**
AVL trees are named after their inventors Adelson, Velski and Landis (AVL). These are height balancing binary trees.
An AVL tree can be defined as a tree in which each node is assigned with a balance factor which is calculated by subtracting the height of the left subtree with the height of the right subtree. The tree is said to be balanced if the balance factor is either -1, 0, or 1 (between -1 and 1, inclusive).

***Balance factor: height(left_subtree) - height(right_subtree)***
