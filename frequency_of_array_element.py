array1=[1,2,3,1,2,5,6,1]
frequency={}
for i in array1:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
for i,frequency in frequency.items():
    print(f"Element {i} in apperance {frequency}")

# counts=counts(array1)
