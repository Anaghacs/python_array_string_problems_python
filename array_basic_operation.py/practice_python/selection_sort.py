arr1=[100,20,50,30,70,5]
print("Orginal array :",arr1)
n=len(arr1)
for i in range(n):
    mids=i
    for j in range(i+1,n):
        if arr1[mids]>arr1[j]:
            mids=j
    arr1[i],arr1[mids]=arr1[mids],arr1[i]
print("Sorted array using selection sort :",arr1)