def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr
n = int(input())
count = 0
i = 0
arr = [int(i) for i in input().split()]
while(i < n):
    if arr[i] == i+1:
        i += 1
        continue
    arr = swap(arr,i,arr[i]-1)
    count += 1
print(count)
print(arr)