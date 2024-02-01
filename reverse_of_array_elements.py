size=int(input("Enter ur size :"))
array1=[]
for i in range(size):
    elements=int(input("Enter the elements in an array :"))
    array1.append(elements)
print("Array elements : ",array1)
size1=len(array1)
for i in range(size1//2):
    temp=array1[i]
    array1[i]=array1[size1-i-1]
    array1[size1-i-1]=temp
print("Reverse of an array elements :",array1)