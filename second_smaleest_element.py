def second_smallest_element(s,arr):
    s=len(arr)
    largest=0
    second_largest=0
    third=0
    for i in arr:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest and i!=largest:
            second_largest=i
        elif i>third and i!=second_largest and i!=largest:
            third=i
    return second_largest,largest,third

size=int(input("Enter your array size : "))
array1=[]
for i in range(size):
    elements=int(input("Enter your array elements : "))
    array1.append(elements)
print("Orginal array elements : ",array1)
result,largest,third=second_smallest_element(size,array1)
print("first largest :",largest)
print("second largest :",result)
print("third largest :",third)