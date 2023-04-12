class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_successor(root, node):
    if node.right is not None:
        # Jeśli węzeł ma prawe dziecko, to następnikiem jest najmniejszy węzeł w prawym poddrzewie
        current = node.right
        while current.left is not None:
            current = current.left
        return current.value

    # Jeśli węzeł nie ma prawego dziecka
    # To następnikiem jest pierwszy przodek, którego lewe poddrzewo zawiera dany węzeł
    successor = None
    current = root
    while current is not None:
        if node.value < current.value:
            successor = current
            current = current.left
        elif node.value > current.value:
            current = current.right
        else:
            break

    return successor.value


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

# Testowanie
print(tree_successor(root, root.left))  # 6
print(tree_successor(root, root))  # 15
print(tree_successor(root, root.left.left.right))  # 4
