def upper_decor(func):
    def wrapper(n):
        result=func(n)
        return result.upper()
    return wrapper

def attach_length(func):
    def wrapper(sent):
        result=func(sent)
        length=len(result)
        result+=str(length)
        return result
    return wrapper

#decorator chaining

@upper_decor
@attach_length
def hello_name(name):
    return 'hello '+name

print(hello_name("anagha "))
