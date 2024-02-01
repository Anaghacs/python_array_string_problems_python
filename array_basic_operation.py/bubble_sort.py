def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swap=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
        if swap==False:
            break
            
arr1=[64,34,25,12,22,11,90]
print("Orginal array :",arr1)
bubble_sort(arr1)
print("sorted array :",arr1)