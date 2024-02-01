def triple_decor(func):
    def inner_function(inputs):
        any_list=func(inputs)
        return [item*3 for item in any_list]
    return inner_function
            
        
@triple_decor
def reverse(l):
    return l[::-1]
 
@triple_decor
def upper_list(l):
    return [item.upper() for item in l]
    
@triple_decor
def fibnocci(n):
    result=[]
    a,b=0,1
    while b<=n:
        result.append(b)
        a,b=b,a+b
    return result
        
print(reverse([1,2,3,4,5]))
print(upper_list(['a','b','c']))
print(fibnocci(6))