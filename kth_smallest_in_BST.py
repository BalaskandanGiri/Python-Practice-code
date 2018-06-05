from treenode import tree
count = 0
def inorder(node):
    global count
    if node:
        inorder(node.left)
        count += 1
        if count == 3:
            print(end="--")
        print(node.data,end=" ")
        inorder(node.right)
inorder(tree.root)