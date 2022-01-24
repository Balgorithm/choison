## input
## 5 3
## 1 3 2 3 2
## output
## 8

## input
## 8 5
## 1 5 4 3 2 4 5 2
## output
## 25

n,m = map(int,input().split())
ball = sorted(list(map(int,input().split())))

## 1 2 2 3 3
cnt = 0
for i in range(n-1):
    for j in range(i+1,n):
       if ball[i] != ball[j]:
           cnt+=1
print(cnt)
