from collections import deque

N=int(input())
M=int(input())
A=[[] for _ in range(N+1)]
for i in range(M):
    x,y,w=map(int,input().split())
    A[x].append((y,w))
start,end=map(int,input().split())

def dijkstra():
    vis = [-1] * (N + 1)
    vis[start]=0
    q=deque()
    q.append(start)
    while q:
        x=q.popleft()
        for y,w in A[x]:
            if vis[y]==-1:
                vis[y]=vis[x]+w
                q.append(y)
            elif vis[y]>vis[x]+w:
                vis[y] = vis[x] + w
                q.append(y)
    return vis[end]
print(dijkstra())
