from collections import deque

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    d = []
    n = len(food_times)
    for i in range(1, n + 1):
        d.append([i, food_times[i - 1]])
    dq = deque(sorted(d, key=lambda x: x[1]))
    answer=0
    total_eat, last_eat = 0,0
    while (1):
        to_eat = (dq[0][1] -last_eat) * len(dq)
        if total_eat + to_eat > k:
            dq = sorted(dq,key=lambda x : x[0])
            break
        total_eat += to_eat
        last_eat = dq[0][1]
        dq.popleft()
    print(dq)
    print(k-total_eat)
    answer = dq[(k-total_eat)%len(dq)][0]
    return answer


print(solution([3,1,2],5))  ##1
print(solution([3, 1, 2, 4, 5],10))  ##4
print(solution([3, 1, 2],10))  ##2
print(solution([3,4,5,6,7],15))  ## -1
print(solution([3,4,5,6,7],10))  ##1
print(solution([3,4,5,6,7],20))  ##4
print(solution([3,4,5,6,7],8))  ##4
print(solution([7,6,5,4,3],10))  ##1
print(solution([4,5,6,7,8],20))  ##2
