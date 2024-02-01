# list1=[1,2,3,4,5,6]

# print("Orginal list elements : ",list1)
# squres=[i*i for i in list1]
# print("Square of the list elements : ",squres)

list1=[]
size=int(input("Enter your size of the list :"))
for i in range(size):
    elements=int(input("Enter the elements in an list : "))
    list1.append(elements)
print("Orginal list elements : ",list1)
sqrues=[i*i for i in list1]
print("Square of the list elemnts :",sqrues)