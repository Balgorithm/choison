## 4 6
## 19 10 15 17
## result = 6

n, target = map(int,input().split())

duck = list(map(int,input().split()))
duck.sort()
start = 0
end = duck[-1]

while(start<=end):
    temp = 0
    mid = (start+end)//2
    for i in duck:
        if i>mid:
            temp += i-mid

    if temp >= target:
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)
