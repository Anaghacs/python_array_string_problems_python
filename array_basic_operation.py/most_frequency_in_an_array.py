def count_freqency(arr,n):
    maxcount=0
    element_array=0
    for i in range(0,n):
        counts=0
        for j in range(0,n):
            if arr[i]==arr[j]:
                counts+=1
        if counts>maxcount:
            maxcount=counts
            element_array=arr[i]
        return element_array,counts

arr1=[10,20,10,30,10,40]
n=len(arr1)
print("Array elements :",arr1)
element,count=count_freqency(arr1,n) 
print("Duplicate element : ",element)
print("Total count : ",count)


