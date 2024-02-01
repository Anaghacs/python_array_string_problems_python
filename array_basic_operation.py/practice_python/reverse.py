arr1=[10,20,30,40,50]
print("Orginal array :",arr1)
n=len(arr1)
start=0
end=n-1
while start<end:
    arr1[start],arr1[end]=arr1[end],arr1[start]
    start+=1
    end-=1
print("Reversed array :",arr1)
