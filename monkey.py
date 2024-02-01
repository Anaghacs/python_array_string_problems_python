array1=[1,2,1,3,4,1]
n=len(array1)
print(array1)
value=4

# for i in array1:
#     count=0
#     if i==value :
#         count+=1
# for i in array1:
#     count=0
#     for j in range(i+1,n):
#         if i==j:
#             count+=1
# print(count)
new=[]
# for i in range(n):
#     for j in range(i+1,n):
#         if j==value:
#             new.append(j)
# print(new)

for i in range(n):
    if i==value:
        print("element in an array")
    else:
        print("invalid number ")



