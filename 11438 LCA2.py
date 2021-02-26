#euler tour  / + bottom up segement tree
import sys
sys.setrecursionlimit(200001)
N=int(input())

li=[[] for _ in range(100001)]

for i in range(N-1):
    v1,v2=map(int,sys.stdin.readline().split())
    li[v1].append(v2)
    li[v2].append(v1)

seg=[[0]*200001 for i in range(20)]
index=[0]*100001
he=[0]*100001
x=0
def tour(v,p,h):
    global x
    seg[0][x]=v
    index[v]=x
    he[v]=h
    x+=1
    for i in li[v]:
        if i==p:
            continue
        tour(i,v,h+1)
        seg[0][x] = v
        x += 1
tour(1,0,0)

i=1
while seg[i-1][0]:
    j=0
    while seg[i-1][j] and seg[i-1][j+2**(i-1)]:
        if he[seg[i-1][j]] <he[seg[i-1][j+2**(i-1)]]:
            seg[i][j]=seg[i-1][j]
        else:
            seg[i][j]=seg[i-1][j+2**(i-1)]
        j+=1
    i+=1

M=int(input())
for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    ans = v1
    v1,v2=index[v1],index[v2]
    dif=abs(v2-v1)+1
    cur = min(v1,v2)
    j = 0
    while dif:
        if dif & 1:
            if he[ans]>he[seg[j][cur]]:
                ans=seg[j][cur]
            cur+=2**(j)
        dif = dif >> 1
        j+=1
    print(ans)
