from treenode import treenode
from collections import defaultdict

dict = defaultdict(list)

root = treenode(8)
root.left = treenode(3)
root.right = treenode(10)
root.left.left = treenode(1)
root.right.left = treenode(6)
root.right.right = treenode(14)
root.right.right.left = treenode(13)
root.right.left.left = treenode(4)
root.right.left.right = treenode(7)

def diagonaltraversal(curr,level):
    if curr != None:
        diagonaltraversal(curr.left,level-1)
        dict[level].append(curr.data)
        diagonaltraversal(curr.right, level)
diagonaltraversal(root,0)
print(dict)