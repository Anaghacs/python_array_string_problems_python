def min_max(arr1):
    for i in arr1:
        mins=maxs=arr1[0]
        if i<mins:
            mins=i
        elif i>maxs:
            maxs=i
    # mins=min(arr1)
    # maxs=max(arr1)
    return mins,maxs

arr=[10,20,30,4,50]
print("original array :",arr)
minimum,maximum=min_max(arr)
print(f"Minimum value in an array : {minimum}")
print(f"Minimum value in an array : {maximum}")

