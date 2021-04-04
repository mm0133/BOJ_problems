import sys

N=int(sys.stdin.readline())
sq=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
dp=[[0]*N for _ in range(N)]
for i in range(0,N):
    r=i
    l=i
    while l>=0 and r<N and sq[r]==sq[l]:
        dp[l][r]=1
        r+=1
        l-=1
    r = i + 1
    l = i
    while l >= 0 and r < N and sq[r] == sq[l]:
        dp[l][r] = 1
        r += 1
        l -= 1

for i in range(M):
    s,e=map(int,sys.stdin.readline().split())
    print(dp[s-1][e-1])