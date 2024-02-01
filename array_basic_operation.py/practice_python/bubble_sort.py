arr1=[250,30,450,5,100,400,100]
print("Original array :",arr1)
n=len(arr1)
for i in range(n):
    for j in range(0,n-i-1):
        if arr1[j]>arr1[j+1]:
            arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
print("Bubble sorted array :",arr1)