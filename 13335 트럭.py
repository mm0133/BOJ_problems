from collections import deque

N,W,L= map(int,input().split())
A=list(map(int, input().split()))
q=deque()

a=1
t=0
sm=A[0]
q.append((W+1,A[0]))
while q:
    t += 1
    if q[0][0] <= t:
        tem=q.popleft()
        sm-=tem[1]
    if a<N:
        if sm+A[a]<=L:
            sm+=A[a]
            q.append((t+W,A[a]))
            a+=1
print(t)
