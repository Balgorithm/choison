import heapq,sys

n = int(sys.stdin.readline())
lecture =[]
for _ in range(n):
    start,end =sys.stdin.readline().split()
    lecture.append([int(start),int(end)])
q=[]
lecture = sorted(lecture,key=lambda x : (x[0],x[1]))
heapq.heappush(q,lecture[0][1])
for i in range(1,n):
    if lecture[i][0] < q[0]:
        heapq.heappush(q,lecture[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q,lecture[i][1])

print(len(q))
