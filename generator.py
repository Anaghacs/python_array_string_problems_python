def generator1():
    yield 10
    yield 20
    yield 30
x=generator1()
print(next(x))
print(next(x))