
size=int(input("Enter your size : "))
array1=[]
for i in range(size):
    elements=int(input("Enter array elements : "))
    array1.append(elements)
print("Orginal array : ",array1)
array1.append(None)

pos=int(input("Enter new element position in an array : "))
value=int(input("Enter new element value : "))
# array1.insert(pos,value)
# print("New array : ",array1)

for i in range(len(array1)-1,pos-1,-1):
    array1[i]=array1[i-1]
array1[pos]=value

print(array1)
