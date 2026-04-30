class Node:
    def __init__(self, value,files):
        self.back = None
        self.next = None
        self.value = str(value)
        self.files=files

def adds(node, value,files):
    current = node
    while current.next is not None:
        current = current.next

    new_node = Node(value,files)
    new_node.back = current
    current.next = new_node

def lists(node):
    current = node
    while current is not None:
        print(current.value)
        print(current.files)
        current = current.next
files=b''
ffiles=''
for a in range(0,255):
    ffiles=ffiles+chr(a)
files=ffiles.encode()
# criar lista
root = Node("root",files)

for a in range(10):
    adds(root, "node " + str(a),files)


lists(root)