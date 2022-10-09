n = int(input())
array = list(map(int,input().split()))
m = int(input())
array_m = list(map(int,input().split()))

start=0
end = len(array) - 1

def binary_search(array, target, start, end):
    while(start<=end):
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        else:
            if array[mid]>target:
                end = mid-1
            else:
                start= mid+1

for i in array_m:
    start = 0
    end = len(array)-1
    if binary_search(array,i,start,end):
        print("yes",end= " ")
    else:
        print("no",end= " ")
