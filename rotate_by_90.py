arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]
n = len(arr)
for layer in range(0,int(n/2)):
    first = layer
    last = n - 1 - first
    for i in range(first,last):
        top = arr[first][i]
        offset = i - first
        arr[first][i] = arr[last-offset][first]
        arr[last-offset][first] = arr[last][last-offset]
        arr[last][last-offset] = arr[i][last]
        arr[i][last] = top
for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j],end=" ")
    print()