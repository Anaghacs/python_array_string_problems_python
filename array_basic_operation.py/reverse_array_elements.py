# def reverse_array(arr):
#     n=len(arr)
#     start=0
#     end=n-1
#     while start<end:
#         arr[start],arr[end]=arr[end],arr[start]
#         start+=1
#         end-=1

# arr1=[10,20,30,40,50,60,100]
# print("Orginal array :",arr1)
# reverse_array(arr1)
# print("Reverse order in an array :",arr1)

arr1=[10,20,30,40]
print("Orginal array :",arr1)
n=len(arr1)
start=0
end=n-1
while start<end:
    arr1[start],arr1[end]=arr1[end],arr1[start]
    start+=1
    end-=1
print("Reversed array :",arr1)
