class _Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self, e):
        newnode = _Node(e, None)
        if self.isempty():
            self._head = newnode
        else:
            self._tail._next = newnode
        self._tail = newnode
        self._size += 1
        
    # to insert a node at the first position    
    def addfirst(self, e):
        newnode = _Node(e, None)
        if self.isempty():
            self._head = newnode
        else:
            newnode._next = self._head
        self._head = newnode
        self._size += 1
        
        # to insert a node in between the linked list
    def addbetween(self, e):
        newnode = _Node(e, None)
        if self.isempty():
            self._head = newnode
        else:
            position=(int(input("Enter the position of the node to be inserted:")))
            temp = self._head
            for nodeno in range(1, len(L)):
                if(nodeno != position):
                    temp = temp._next
                else:
                    newnode._next = temp._next
                    temp._next = newnode
                    self._size += 1
                    break
        
    def display(self):
        temp = self._head
        while temp:
            print(temp._element,end='--> ')
            temp = temp._next
        print()
L = LinkedList()   # L is an instance of linked list
print("length of linked list is",len(L))
L.addlast(10)   # creates first node
L.addlast(20)   # creates second node
L.addlast(30)  # creates third node
L.addlast(40)   # creates fourth node
L.addlast(50)   # creates fifth node
L.display()    # print elements of each node of a linked list
L.addfirst(1000)
L.display()
L.addfirst(2000)
L.display()
L.addbetween(35)
print("Linked list elements after insertion of new node between first and last nodes")
L.display()
print('Size:',len(L))
