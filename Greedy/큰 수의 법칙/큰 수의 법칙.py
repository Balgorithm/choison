###배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 같은 수는 한번에 연속 k번 초과하여 더해질 수 없다.

n,m,k = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()

answer = num_list[-1] * (m//k)*k + num_list[-2] * (m%k)

print(answer)


2022/09/28
n,m,k = map(int,input().split())
num = list(map(int,input().split()))
num.sort(reverse=True)
x = m//k
y = m%k
answer = 0
answer+=num[0]*x*k
answer+=num[1]*y

print(answer)
