# n , target

n,target = map(int,input().split())
num = list(map(int,input().split()))
ans = 0

start = 0
end = len(num)-1
def binary_search(target,start,end):
    global ans
    mid = (start+end)//2
    ans+=1
    if start>end:
        return None
    elif num[mid] ==target:
        return ans
    else:
        if num[mid] > target:
            return binary_search(target,start,mid-1)
        else:
            return binary_search(target,mid+1,end)

print(binary_search(target,start,end))
