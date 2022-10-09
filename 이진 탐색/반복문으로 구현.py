# n , target
n,target = map(int,input().split())
num = list(map(int,input().split()))

ans=0
start = 0
end = len(num)-1
while(start<=end):
    print(start,end)
    mid = (start+end)//2
    ans+=1
    if num[mid] == target:
        print(ans)
        break
    else:
        if num[mid]>target:
            end = mid-1
        else:
            start= mid+1
