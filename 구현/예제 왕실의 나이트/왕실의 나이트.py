knight = input()

chess = [[0]*8 for _ in range(8)]
d = {}
for i in range(97,105):
    d[str(chr(i))] = i-97

###   {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

x,y = d[knight[0]],int(knight[1])-1
answer=0

if x-2 >=0:  ######
    if y-1>=0:
        answer+=1
    if y+1 <=7:
        answer+=1
if x+2<=7:
    if y-1>=0:
        answer+=1
    if y+1 <=7:
        answer+=1
if y+2<=7:
    if x-1>=0:
        answer+=1
    if x+1 <=7:
        answer+=1
if y-2>=0:
    if x-1>=0:
        answer+=1
    if x+1 <=7:
        answer+=1

print(answer)
