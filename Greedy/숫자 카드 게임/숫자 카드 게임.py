### n * m 행렬

n,m = map(int,input().split())

answer = 0
for _ in range(n):
    d= list(map(int,input().split()))
    if min(d) > answer:
        answer = min(d)

print(answer)
