def my_concate(lt1,lt2):
    lt1.extend(lt2)
    return lt1

lst1=[1,2,3,4]
lst2=[5,6,7,8,9,10]
print("First list item :",lst1)
print("Second list item :",lst2)
result=my_concate(lst1,lst2)
print("Concatinate two list :",result)