test=int(input())
for t in range(test):
    n=int(input())
    arr=[int(i) for i in input().split()]
    a,b=0,0
    for i in arr:
        if i+a > 0:
            a = i+a
        if a > b:
            b = a
