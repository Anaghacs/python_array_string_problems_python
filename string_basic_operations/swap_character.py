st1="hello anagha"
print("Orginal string :",st1)
index1=1
index2=3
characters=list(st1)
characters[index1],characters[index2]=characters[index2],characters[index1]
ns=str(characters)
print(ns)