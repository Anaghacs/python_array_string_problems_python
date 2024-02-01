def insert_element(arr,val,posit):
    n=len(arr)
    for i in range(posit,n-1):
        if arr[i]==val:
            arr[i]=arr[i+1]
            
arr1=[10,20,30,40,50]
print("Orginal array :",arr1)
value=int(input("Enter specific value :"))
position=int(input("Enter your current new value position :"))
insert_element(arr1,value,position)
print(arr1)