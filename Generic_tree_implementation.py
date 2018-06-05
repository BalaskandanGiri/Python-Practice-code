

class node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None

root=node(10)
root.left=node(5)
root.right=node(15)
root.left.left=node