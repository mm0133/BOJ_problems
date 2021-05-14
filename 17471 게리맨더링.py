from collections import deque
from itertools import combinations

N=int(input())
A=list(map(int, input().split()))
adj=[[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    tem=list(map(int,input().split()))
    for j in tem[1:]:
        adj[i][j]=1
        adj[j][i]=1

def bfs(Z):
    q=deque()
    q.append(Z[0])
    vis[Z[0]]=1
    while q:
        x=q.pop()
        for to in Z:
            if vis[to]==0 and adj[x][to]==1:
                vis[to]=1
                q.append(to)



answer=1001
all=[i for i in range(1,N+1)]
for t in range(1,N//2+1):
    com=combinations(all,t)
    for X in com:
        Y=[]
        for i in all:
            if not i in X:
                Y.append(i)

        vis=[0]*(N+1)
        bfs(X)
        bfs(Y)
        if sum(vis)==N:
            s1=0
            s2=0
            for i in all:
                if i in X:
                    s1+=A[i-1]
                else:
                    s2+=A[i-1]
            answer=min(answer,abs(s1-s2))
if answer==1001:
    answer=-1
print(answer)