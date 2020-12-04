class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

def build_product_tree():
    root = Node("Electronics")

    laptop = Node("Laptop")
    laptop.add_child(Node("Asus"))
    laptop.add_child(Node("Lenovo"))
    laptop.add_child(Node("MacBook"))

    cell = Node("Cell Phone")
    cell.add_child(Node("Redmi"))
    cell.add_child(Node("Samsung"))
    cell.add_child(Node("iPhone"))

    tv = Node("Television")
    tv.add_child(Node("LG"))
    tv.add_child(Node("Sony"))

    root.add_child(laptop)
    root.add_child(cell)
    root.add_child(tv)

    for d in root.children:
      print("Children of the root node:", d.data)
    print("\n")
    for l in laptop.children:
      print("Children of Laptop node:", l.data)
    print("\n")
    for c in cell.children:
      print("Children of Cell Phone node:", c.data)
    print("\n")
    for t in tv.children:
      print("Children of Television node:", t.data)


build_product_tree()

'''
OUTPUT: 
Children of the root node: Laptop
Children of the root node: Cell Phone
Children of the root node: Television


Children of Laptop node: Asus
Children of Laptop node: Lenovo
Children of Laptop node: MacBook


Children of Cell Phone node: Redmi
Children of Cell Phone node: Samsung
Children of Cell Phone node: iPhone


Children of Television node: LG
Children of Television node: Sony
'''