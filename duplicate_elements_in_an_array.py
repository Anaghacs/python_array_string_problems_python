size=int(input("Enter your array size : "))
array1=[]
dupli=[]
for i in range(size):
    elements=int(input("Enter your array elements : "))
    array1.append(elements)
print("Orginal array : ",array1)
for i in range(len(array1)):
    for j in range(i+1,len(array1)):
        if array1[i]==array1[j] :
            dupli.append(array1[i])             
print(dupli)
print(array1)
