arr1=[60,20,40,1,5]
print("orginal array :",arr1)
n=len(arr1)
for i in range(n):
    for j in range(0,n-i-1):
        if arr1[j]>arr1[j+1]:
            arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
print("Bubble sort :",arr1)