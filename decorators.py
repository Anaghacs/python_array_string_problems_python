def upper_decor(fun):
    def wraper():
        result=fun()
        return result.upper()
    return wraper

def hello():
    return "Hello good morning"

f=upper_decor(hello)
print(f())

#other method in decorator direct call withput decorator function and decorate function 
# using '@'
# function_name and with argument and function
def upper_dec(funct):
    def f1(name):
        result=funct(name)
        return result.upper()
    return f1
        
@upper_dec
def hello(name):
    return "hello good morning "+name
print(hello("anagha"))










