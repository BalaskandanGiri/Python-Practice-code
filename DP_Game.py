def game(arr,i,n):
    if i > n:
        return 0
    return max(arr[i]+min(game(arr,i+2,n),game(arr,i+1,n-1)),arr[n]+min(game(arr,i,n-2),game(arr,i+1,n-1)))
arr = [8,7,15,1,22,10]
print(game(arr,0,len(arr)-1))