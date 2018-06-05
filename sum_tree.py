class node:
    def __init__(self,d):
        self.left=None
        self.right=None
        self.data=d
root=node(10)
root.left=node(5)
root.right=node(15)
root.left.left=node(3)
root.left.right=node(7)

def func(node):
    if node==None:
        return 0
    curr=node.data
    node.data=func(node.left)+func(node.right)
    return curr+node.data
func(root)
print(root.left.data,root.data)