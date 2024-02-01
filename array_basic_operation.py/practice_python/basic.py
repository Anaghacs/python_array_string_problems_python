#reverse array elements in an array
# arr1=[10,20,30,40,50]
# print("Orginal array : ",arr1)
# n=len(arr1)
# star=0
# end=n-1
# while star<end:
#     arr1[star],arr1[end]=arr1[end],arr1[star]
#     star+=1
#     end-=1
# print(arr1)

#selection sort in an array

# arr1=[100,20,50,80,5,65,70,10]
# print("Orginal array :",arr1)
# n=len(arr1)
# for i in range(0,n):
#     mids=i
#     for j in range(i+1,n):
#         if arr1[mids]>arr1[j]:
#             mids=j
#     arr1[i],arr1[mids]=arr1[mids],arr1[i]
# print("Selection sorted array :",arr1)

#binary searching in an array 

# arr1=[10,20,30,40,50,60,100]
# print("Orginal array :",arr1)
# n=len(arr1)
# value=30
# start=0
# end=n-1
# found=False
# while start<end:
#     mid=start+end//2
#     if arr1[mid]==value:
#         found=True
#         break
#     elif arr1[mid]<value:
#         start=mid+1
#     else:
#         end=mid-1
# if found==True:
#     print(f"The element {value} is found in {mid}")
# else:
#     print(f"The element {value} is not found in {mid}")

#insert new element
#  in an array
# arr1=[10,20,30,40,50]
# value=100
# position=2
# n=len(arr1)
# for i in range(n-1,position-1,-1):
#     arr1[i]=arr1[i-1]
# arr1[position]=value
# print("New array :",arr1)

#find even or odd in an array 
arr1=[10,20,30,40,50,60]
print("Orginal array :",arr1)
even=[item for item in arr1 if item%2!=0]
print("Even numbers :",even)




