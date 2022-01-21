# input
# 5
# 2 3 1 2 2
# output
# 2

n=int(input())
fear = list(map(int,input().split()))

fear = sorted(fear)
temp =0
answer = 0
for i in fear:
    temp+=1
    if temp >= i:
        answer+=1
        temp = 0

print(answer)
