n,k= map(int,input().split())

answer= 0

while(1):
    if n%k !=0:
        answer+=1
        n-=1
    else:
        n /=k
        answer+=1
    if n == 1:
        break
print(answer)
