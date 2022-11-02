class DList:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.head = self.Node(None)
        self.tail = self.Node(None, self.head)
        self.head.next = self.tail
        self.cur = self.tail

    def insert(self,node,value):
        left = node.left
        new_node = self.Node(value, left, node)
        node.left = new_node
        left.right = new_node

    def delete(self,node):
        left = node.left
        right = node.right
        left.right = right
        right.left = left

    def print_nodes(self):
        node = self.head.right
        while node!=self.tail:
            if node.right != self.tail:
                print(node.value)
            else:
                print(node.value)
        node = node.right

data = list(input())

m = int(input())

orders = [
    tuple(input().split())
    for _ in range(m)
]

dl = DList()
for i in range(len(data)):
    dl.insert(dl.tail,data[i])

for order in orders:
    if order[0] == "L":
        if dl.cur.left.left != None:
            dl.cur = dl.cur.left
    elif order[0] == "D":
        if dl.cur.right != None:
            dl.cur = dl.cur.right
    elif order[0] == "B":
        if dl.cur.left.left != None:
            dl.delete(dl.cur.left)
    else:
        dl.insert(dl.cur,order[1])

dl.print_nodes()