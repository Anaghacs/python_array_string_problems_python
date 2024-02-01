size=int(input("Enter your size : "))
array1=[]
for i in range(size):
    elements=int(input("Enter array elemnts : "))
    array1.append(elements)
print(array1)
prime=[]
not_prime=[]
for i in (array1):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag+=1
    if flag==0:
        prime.append(i)
    else:
        not_prime.append(i)
print("Prime numbers in an array : ",prime)
print("Not a prime numbers in array : ",not_prime)



