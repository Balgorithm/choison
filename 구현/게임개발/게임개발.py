# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

n, m = map(int,input().split())
x,y,idx = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]
ans = 0
graph[x][y] = 1
ans+=1
rotate_cnt = 0
rotate_temp = False
while(1):
    # print("x: ",x,"y: ",y,"idx: ",idx)
    # print('rotate_cnt: ',rotate_cnt)
    idx = (idx+1) % 4
    rotate_cnt+=1
    nx = x + dx[idx]
    ny = y + dy[idx]

    if 0<=nx<n and 0<=ny<m:
        if graph[nx][ny] ==0:
            ans+=1
            graph[nx][ny] = 2
            x,y = nx,ny
            rotate_cnt=0
            continue
        if rotate_cnt==4:
            rotate_cnt=0
            idx = (idx+1)%4
            nx,ny = x + dx[idx], y+dy[idx]
            if graph[nx][ny] ==1:
                break
            x,y = nx,ny

print(ans)
