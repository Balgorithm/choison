
def solution(s):
    ans_list=[]
    if len(s)==1:
        return 1
    for x in range(1,len(s)):
        d=[]
        for i in range(0,len(s),x):
            if i+x<len(s):   
                d.append(s[i:i+x])
            else:
                d.append(s[i:])
        num = [1]* len(d)
        idx = 0
        tmp = 0
        dist= 0
        while(idx < len(d)-1):
            if d[idx] == d[idx+1]:
                num[tmp]+=1
            else:
                tmp = idx+1
            idx+=1
            
        ans=[]
        ans.append(d[0])
        for i in range(1,len(d)):
            if d[i] != ans[-1]:
                ans.append(d[i])
        real_answer= ''
        for i in ans:
            real_answer+=i
        for i in num:
            if i != 1:
                real_answer+=str(i)
        ans_list.append(real_answer)

    min = 1000
    for i in ans_list:
        if len(i)<=min:
            min = len(i)
    return min
