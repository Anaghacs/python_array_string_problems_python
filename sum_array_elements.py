# size=int(input("Enter your size : "))
# array1=[]
# sum=0
# for i in range(size):
#     elements=int(input("Enter elements in an array : "))
#     array1.append(elements)
    
# for item in array1:
#     sum=sum+item

# print("Array elements : ",array1)
# print("Sum of array elements : ",sum)

# function to create sum of all elemnets in an array.

def add(arr):
    global sum
    for item in arr:
        sum=sum+item
    return sum

size=int(input("Enter your size : "))
array1=[]
sum=0
for i in range(size):
    elements=int(input("Enter elements in an array : "))
    array1.append(elements)
res=add(array1)  
print("Array elements : ",array1)
print("Sum of array elements : ",res)


 
# size=int(input("Enter your size :"))
# array1=[]
# sum=0

# for i in range(size):
#     elements=int(input("Enter the elements in an array :"))
#     array1.append(elements)
# print(array1)

# def sum_array_elements(arr1):
#     sum=0

#     for i in arr1:
#         sum=sum+i

# add=sum_array_elements(array1)
# print("sum of all array elemnts :",sum)


