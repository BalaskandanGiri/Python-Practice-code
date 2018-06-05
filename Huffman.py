class huffman_node:
        def __init__(self,n,d):
            self.left = None
            self.right = None
            self.name = n
            self.data = d
        def __str__(self):
            return str(self.name) + "-" + str(self.data)
        def __repr__(self):
            return str(self.name)+ "-"+str( self.data)
        def __lt__(self, other):
            return self.data < other.data

l = list()
l.append(huffman_node("a",5))
l.append(huffman_node("b",9))
l.append(huffman_node("c",12))
#l.append(huffman_node("d",1))

while(len(l)!=1):
    a = l.pop(0)
    b = l.pop(0)
    c=huffman_node("internal node",a.data + b.data)
    c.left = a
    c.right = b
    l.append(c)
print(l)

def func(node,string):
    if node:
        func(node.left,string+"0")
        print(node,"--",string)
        func(node.right,string+"1")
func(l[0],"")