size=int(input("Enter your array size : "))
array1=[]
for item in range(size):
    elements=int(input("Enter your array elements : "))
    array1.append(elements)
print("Orginal array : ",array1)
value=int(input("Enter your deleted element in an array : "))
new_array=[item for item in array1 if item!=value]
print("Deleted array : ",new_array)

# for i in array1:
#     if i==value:
#         array1.remove(i)
