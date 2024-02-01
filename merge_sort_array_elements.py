array1,array2=[10,40,70,30,20],[100,80,5,15,1]
# array2=[100,80,5,15,1]
new=[]
print("Two arrays :",array1,array2)
new=array1+array2
print("Merged array : ",new)
# print(new.sort())
for i in range(0,len(new)):
    for j in range(i+1,len(new)):
        if new[i]>=new[j]:
            new[i],new[j]=new[j],new[i]
            
print("Sorted array elemenrs : ",new)

