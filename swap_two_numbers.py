# a,b=10,20
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

size=int(input("Enter your array size :"))
array1=[]
for i in range(size):
    elements=int(input("Enter your array elements :"))
    array1.append(elements)
print("Orginal array : ",array1)
for i in range(size):
    for j in range(i+1,size):
        if(array1[i]<array1[j]):
            temp=array1[i]
            array1[i]=array1[j]
            array1[j]=temp
print(array1)