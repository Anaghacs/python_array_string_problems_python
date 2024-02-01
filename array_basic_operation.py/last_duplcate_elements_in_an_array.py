def dupliacte(arr1,n):
    for i in range(n-1,0,-1):
        if arr1[i]==arr1[i-1]:
            print(f"Last index of an array {i} and duplicate value {arr[i]}")
    return

arr=[10,20,30,40,40,50]
print("Orginal array :",arr)
n=len(arr)
dupliacte(arr,n)
