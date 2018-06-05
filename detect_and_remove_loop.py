class node:
    def __init__(self, d):
        self.next = None
        self.data = d

    def __str__(self):
        print(str(self.data))


head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
head.next.next.next.next = node(5)
head.next.next.next.next.next = head.next


def findloop(head):
    c1=head
    c2=head
    c1 = c1.next
    c2 = c2.next.next
    while c1 != None and c2 != None and c1 != c2:
        c1 = c1.next
        c2 = c2.next.next
    if c1 == c2:
        return c1

def findloopbeg(head,det):
    while head != det :
        head = head.next
        det = det.next
    return head

findloop = findloop(head)
print("loop detected at - ",findloop.data)
findloopbeg = findloopbeg(head,findloop)
print("loop begenning at - ",findloopbeg.data)

