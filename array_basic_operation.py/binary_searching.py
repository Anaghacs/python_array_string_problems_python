# function definition
def binary_searching(arr,value):
    start=0
    end=len(arr)-1
    mid=(start+end)//2
    # Check if x is present at mid
    if arr[mid]==value:
        return mid
    
    # If x is greater, ignore left half
    elif arr[mid]<value:
        start=mid+1

    # If x is smaller, ignore right half
    else:
        end=mid-1

    # If we reach here, then the element
    # was not present
    return -1

arr1=[10,20,30,40,50,60]
target=30

# Function call
result=binary_searching(arr1,target)
if result!=-1:
    print(f"{target} value is present in an array")
else:
    print(f"{target} value is not present in an array")

