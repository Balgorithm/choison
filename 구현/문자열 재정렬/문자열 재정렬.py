s= input()

s=sorted(s)
num =0
st = ''
for i in s:
    if ord(i)>=48 and ord(i)<=57:
        num+= int(i)
    else:
        st +=i

print(st+str(num))
