str1="hello"
print("Orginal string:",str1)
n=str1[::-1]
if str1==n:
    print(f"The '{str1}' string is palindrome")
else:
    print(f"The '{str1}' string is not palindrome")