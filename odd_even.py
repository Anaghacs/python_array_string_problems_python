size=int(input("Enter ur size :"))
array1=[]
for i in range(size):
    elements=int(input("Enter the lemenets of an array : "))
    array1.append(elements)
print("Array elements : ",array1)
even=[item for item in array1 if item%2==0]
print("Even elements in an array : ",even)
odd=[i for i in array1 if i%2!=0]
print("Odd elemenets in an array : ",odd)

