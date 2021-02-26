from copy import deepcopy
from itertools import combinations

N,M,D=map(int, input().split())
ma=[]
for i in range(N):
    ma.append(list(map(int,input().split())))
com=[i for i in range(M)]
com=combinations(com,3)
ori=deepcopy(ma)

def shoot(end,loc,k):
    global D,cnt
    for r in range(1,D+1):
        for j in range(loc-r+1, loc+r):
            i=end+1-r+abs(j-loc)
            if 0<=j<M and 0<=i<=end:
                if ma[i][j]==1:
                    ma[i][j]=k
                    cnt+=1
                    return
                elif ma[i][j]==k:
                    return
ans=0
for c in com:
    ma=deepcopy(ori)
    cnt=0
    x=2
    for end in range(N-1,-1,-1):
        shoot(end,c[0],x)
        shoot(end,c[1],x)
        shoot(end,c[2],x)
        x+=1
    ans=max(cnt,ans)
print(ans)