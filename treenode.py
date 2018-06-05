class treenode:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class tree:
    root = treenode(10)
    root.left = treenode(5)
    root.right = treenode(15)
    root.left.left = treenode(3)
    root.left.right = treenode(7)
    root.right.left = treenode(13)
    root.right.right =treenode(17)
    def get_root(self):
        return self.root



