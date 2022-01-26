### input 5
### output 11475
n= int(input())
answer=0
for i in range(0,n+1):
    for j in range(0,60):
        for k in range(0,60):
            if '3' in str(i) or '3' in str(j) or '3' in str(k):
                answer+=1

print(answer)
