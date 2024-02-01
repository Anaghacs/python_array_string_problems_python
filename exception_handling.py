# try:
#     a=int(input("Enter first number :"))
#     b=int(input("Enter second number :"))
#     c=a/b
# except:
#     print("Enter valid input number")
# else:
#     print(c)
# finally:
#     print("Your program is completed  :")

try:
    a=int(input("Enter first number :"))
    b=int(input("Enter second number :"))
    c=a/b
except ZeroDivisionError:
    print("Zero division error! not allowed zero")
except ValueError:
    print("Please eneter valid input inuputer not allowed alphabets")
else:
    print(c)
finally:
    print("Progam successfully completed")