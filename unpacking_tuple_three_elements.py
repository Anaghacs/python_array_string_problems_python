def my_sum(*args):
    result=0
    for i in args:
        result+=i
    return result

list1=[1,2,3]
list2=[4,5]
list3=[6,7,8,9,10]
print(my_sum(*list1,*list2,*list3))
