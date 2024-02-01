def count_occurence(arr,value):
    count=0
    for i in arr:
        if i==value:
            count+=1
    return count


array1=[10,20,30,10,40,10]
item=10
print("Orginal array : ",array1)
result=count_occurence(array1,item)
print("Count occurenece of an element : ",result)