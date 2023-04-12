class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_predecessor(root, node):
    if node.left is not None:
        # Jeśli węzeł ma lewe dziecko, to poprzednikiem jest największy węzeł w lewym poddrzewie
        current = node.left
        while current.right is not None:
            current = current.right
        return current.value

    # Jeśli węzeł nie ma lewego dziecka
    # To poprzednikiem jest pierwszy przodek, którego prawe poddrzewo zawiera dany węzeł
    predecessor = None
    current = root
    while current is not None:
        if node.value > current.value:
            predecessor = current
            current = current.right
        elif node.value < current.value:
            current = current.left
        else:
            break

    return predecessor.value

root = Node(15)
root.right = Node(18)
root.right.left = Node(17)
root.right.right = Node(20)
root.left = Node(6)
root.left.right = Node(7)
root.left.right.right = Node(13)
root.left.right.right.left = Node(9)
root.left.left = Node(3)
root.left.left.left = Node(2)
root.left.left.right = Node(4)

print(tree_predecessor(root, root.left)) #4