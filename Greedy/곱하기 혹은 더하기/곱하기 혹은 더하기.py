s = input()
count_0 = 0
count_1 = 0
if s[0] == '0':
    temp ='0'
    count_0 =1
if s[0] == '1':
    temp='1'
    count_1 =1

for i in s[1:]:
    if i != temp:
        if i == '0':
            count_0 +=1
            temp = '0'
        if i == '1':
            count_1 +=1
            temp = '1'

print(min(count_0,count_1))
