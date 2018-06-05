def quick_sort(arr,left,right):
    if left<right:
        a=left
        pivot=left
        b=right
        while a < b:
            while arr[a]<= arr[pivot] and a<=right:
                a+=1
            while arr[b]> arr[pivot]:
                b-=1
            if a < b:
                temp=arr[a]
                arr[a]=arr[b]
                arr[b]=temp
        temp=arr[pivot]
        arr[pivot]=arr[b]
        arr[b]=temp
        quick_sort(arr,left,b-1)
        quick_sort(arr,b+1,right)
arr=[3,5,2,4,1]
quick_sort(arr,0,4)
print(arr)