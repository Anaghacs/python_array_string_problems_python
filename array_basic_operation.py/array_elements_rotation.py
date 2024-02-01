def array_rotation(arr,ds):
    n=len(arr)
    p = 1
    while(p <= ds):
        last = arr[0]
        for i in range (n - 1):
            arr[i] = arr[i + 1]
        arr[n - 1] = last
        p = p + 1

arr1=[10,20,30,40,50,600]
print("Orginal array :",arr1)
ds=3
array_rotation(arr1,ds)
print("Array elements rotation :",arr1)