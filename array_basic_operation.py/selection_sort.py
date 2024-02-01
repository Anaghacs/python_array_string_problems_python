def selection_sort(arr,size):
    for i in range(size):
        for j in range(i+1,size):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
arr1=[1,13,121,0,451,165]
print("orginal array :",arr1)
n=len(arr1)
selection_sort(arr1,n)
print("sorted array using selection sort :",arr1)