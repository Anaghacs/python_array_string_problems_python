
def my_func(arr):
    maximum=0
    minimum=float('inf')
    for i in arr:
        if i>=maximum:
            maximum=i
        if i<=minimum:
            minimum=i
    return maximum,minimum

size=int(input("Enter your array size : "))
array1=[]
for i in range(size):
    elements=int(input("Enter your array elements : "))
    array1.append(elements)
print("Orginal array : ",array1)
max_value,min_value=my_func(array1)
print("Largest element in an array : ",max_value)
print("Minimum number of an array : ",min_value)

# def largest_element(arr):
#     maximum=0
#     for i in arr:
#         if i>=maximum:
#             maximum=i
#     return maximum


# array1=[20,15,33,100,5]
# print("Orginal array elements : ",array1)
# largest=largest_element(array1)
# print("Largest element in an array : ",largest)





