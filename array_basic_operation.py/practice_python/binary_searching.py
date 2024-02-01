arr1=[10,20,30,40,50,60,70]
print("Orginal array :",arr1)
n=len(arr1)
left=0
right=n-1
value=30
found=False
while left<right:
    mids=left+right//2
    if arr1[mids]==value:
        found=True
        break    
    elif arr1[mids]<value:
        left=mids+1
    else:
        right=mids-1
if found:
    print(f"element {value} found at index {mids}")
else:
    print(f"element {value} is not found ")


