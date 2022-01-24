## input
## 1 1 2 3 9
## output
## 8

n = int(input())
coin = sorted(list(map(int,input().split())))

enable = 1

for i in coin:
    if i > enable:
        break
    else:
        enable += i

print(enable)
