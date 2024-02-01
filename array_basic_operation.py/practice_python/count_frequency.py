arr1=[10,20,10,30,20,10,40,50]
print("Orginal array :",arr1)
frequency={}
for i in arr1:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
for i,frequency in frequency.items():
    print(f"the element {i} apperance of {frequency}")

    
