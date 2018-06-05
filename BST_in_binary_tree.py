from treenode import treenode

root = treenode(25)
root.left = treenode(20)
root.left.right = treenode(30)
root.right = treenode(35)
root.right.left = treenode(32)
root.right.right =treenode(40)


class struct:
    def __init__(self,isbst,l,mi,ma):
        self.is_BST = isbst
        self.length = l
        self.mini = mi
        self.maxi = ma

def func(node):
    if node == None:
        return struct(True,0,0,0)
    left = func(node.left)
    right = func(node.right)
    if node.data > right.mini and right.length > 0:
        if left.length > right.length:
            return left
        else:
            return right
    elif node.data < left.maxi and left.length > 0:
        if left.length > right.length:
            return left
        else:
            return right
    if left.is_BST and right.is_BST:
        if left.length == 0:
            mini = node.data
        else:
            mini = left.mini
        if right.length == 0:
            maxi = node.data
        else:
            maxi = right.maxi
        return struct(True,left.length+right.length+1,mini,maxi)
    elif left.is_BST and not right.isBST:
        return struct(False,left.length,0,0)
    else:
        return struct(False,right.length,0,0)
s = func(root)
print(s.length)