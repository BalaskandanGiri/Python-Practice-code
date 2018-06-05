lis = [1,2,2]
s = set()
n = len(lis)
total = pow(2,n)
c = ''
for i in range(total):
    for j in range(n):
        if i & 1<<j:
            c += str(lis[j])
    s.add(c)
    c = ''
print(s)