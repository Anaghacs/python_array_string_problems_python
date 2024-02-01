str1='hello_anagha_good_morning'
print("Orginal string :",str1)
frequency={}
for i in str1:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
n=sorted(frequency.items())
for i,frequency in n:
    print(f"{i} : {frequency}")
