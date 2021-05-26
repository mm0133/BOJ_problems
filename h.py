import sys

N,K=map(int,input().split())
A=[]
for _ in range(N):
    A.append(int(sys.stdin.readline()))
ans=0
if N%2==0:
    for i in range(0,N,2):
        ans+=A[i+1]-A[i]
else:
    no=0
    for i in range(0, N-1, 2):
        no+=A[i+1]-A[i]
        ans=min(no,ans+A[i+2]-A[i+1])
print(ans)
