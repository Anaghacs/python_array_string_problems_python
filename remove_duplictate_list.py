
def remove_duplication(arr):
    result=[]
    for i in arr:
        if i not in result:
            result.append(i)
    return result
my_list=[1,2,2,4,3,4,4,5,6]
print("Orginal array : ",my_list)
result=remove_duplication(my_list)
print("Remove duplication of an array elements : ",result)
