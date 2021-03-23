import sys
from collections import deque

N=int(sys.stdin.readline())
time=[0]*(N+1)
cnt=[0]*(N+1)
adj=[[] for i in range(N+1)]
ans=[0]*(N+1)

for i in range(1,N+1):
    A=list(map(int,sys.stdin.readline().split()))
    time[i]=A[0]
    if len(A)>2:
        for j in A[1:-1]:
            adj[j].append(i)
        cnt[i]=len(A)-2

q=deque([])
for i in range(1,N+1):
    if cnt[i]==0:
        q.append(i)

while q:
    i=q.popleft()
    ans[i]=ans[i]+time[i]
    for j in adj[i]:
        cnt[j]-=1
        ans[j]=max(ans[j],ans[i])
        if cnt[j]==0:
            q.append(j)

for i in range(1,N+1):
    print(ans[i])




