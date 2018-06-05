from treenode import treenode
tail = None
head = None
def func(node):
    global tail,head
    if not node:
        return
    if node.left:
        func(node.left)
    node.left = tail
    if tail:
        tail.right = node
    else:
        head = node
    tail = node
    if node.right:
        func(node.right)



root = treenode(10)
root.left = treenode(5)
root.right = treenode(15)
root.left.left = treenode(2)
root.left.right = treenode(7)

func(root)
while head!= None:
    print(head.data)
    head =  head.right