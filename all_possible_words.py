def func(arr1,arr2):
    if len(arr1)==len(arr2):
        print(arr1)
    else:
        for i in arr2:
            if i not in arr1:
                arr1+=i
                func(arr1,arr2)
                arr1=arr1[:-1]
func("","abc")