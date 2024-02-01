size=int(input("Enter your array size : "))
array1=[]
mul=[]
for i in range(size):
    elements=int(input("Enter array elements : "))
    array1.append(elements)
print("Original array element in  an array :",array1)
mul=[i for i in array1 if i%5==0]
# for i in array1:
#     if i%5==0:
#         mul.append(i)
print("5 Multiples of an array elements : ",mul)