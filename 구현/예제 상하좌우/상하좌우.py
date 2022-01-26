### input
### 5
### R R R U D D

n = int(input())
plan = list(map(str,input().split()))

map= [[0]*(n) for i in range(n)]
x,y = 0,0
for i in plan:
    if i == "R":
        if y <n-1:
            y +=1
    if i == "L":
        if y>0:
            y -=1
    if i == "U":
        if x>0:
            x-=1
    if i == "D":
        if x<n-1:
            x+=1

print(x+1,y+1)
