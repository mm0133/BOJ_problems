import sys
from collections import deque

sys.setrecursionlimit(100001)
N, K= map(int, input().split())
dp=[-1]*100001
dp[N]=0
q=deque()
q.append(N)
while q:
    x=q.popleft()
    if x>0 and dp[x-1]==-1:
        dp[x-1]=dp[x]+1
        q.append(x-1)
    if x<100000 and dp[x+1]==-1:
        dp[x+1]=dp[x]+1
        q.append(x+1)
    if x>1 and x<50001 and dp[2*x]==-1:
        dp[2*x]=dp[x]+1
        q.append(2*x)
    if dp[K]!=-1:
        break
print(dp[K])
