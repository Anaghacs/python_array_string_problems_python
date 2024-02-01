def linear_search(arr,key):
    n=len(arr)
    for i in range(n):
        if arr[i]==key:
            return i
    return -1

arr1=[10,20,30,40,50]
print("Orginal array :",arr1)
target=int(input("Enter the search value :"))
result=linear_search(arr1,target)
if result!=-1:
    print(f"{target} value is presented in the array index is {result}")
else:
    print(f"{target} value is not presented in the array index is {result}")