s = "i like this program very much"
print("Orginal string :",s)
st=list(s)
n=len(s)
start=0
end=n-1
while start<end:
    st[start],st[end]=st[end],st[start]
    start+=1
    end-=1
reverse=''.join(st)
print('Reverse a string : ',reverse)