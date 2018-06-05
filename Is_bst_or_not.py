import math


class node:
    def __init__(self, d):
        self.left = None
        self.right = None
        self.data = d


root = node(10)
root.left = node(5)
root.right = node(15)
root.left.left = node(3)
root.left.right = node(7)


def is_bst(root, mini, maxi):
    if not root:
        return True
    if root.data < mini or root.data > maxi:
        return False

    return is_bst(root.left, mini, root.data) or is_bst(root.right, root.data, maxi)


print(is_bst(root, -100000, 100000))
