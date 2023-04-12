# BST dla node.root
def search_value(root, x):
    if root is None or root.value == x:
        return root
    if x < root.value:
        return search_value(root.left, x)
    else:
        return search_value(root.right, x)


def find_minimum(root):
    if root.left is None:
        return root.value
    return find_minimum(root.left)


def find_maximum(root):
    if root.right is None:
        return root.value
    return find_maximum(root.right)
