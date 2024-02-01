def insert_element(arr,val,posi):
    n=len(arr)
    for i in range(n-1,posi-1,-1):
        arr[i]=arr[i-1]
    arr[posi]=val

arr1=[10,20,30,40,50]
print("Orginal array :",arr1)
value=int(input("Enter specific value :"))
position=int(input("Enter your current new value position :"))
insert_element(arr1,value,position)
print(arr1)