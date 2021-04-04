N,M = map(int, input().split())
m=list(map(int,input().split()))
c=list(map(int,input().split()))
dp=[[0]*10001,[0]*10001]
h=[]
pre=1
cur=0
for i in range(N):
    pre,cur=cur,pre
    for j in range(0,c[i]):
        dp[cur][j]=dp[pre][j]
    for j in range(c[i],10001):
        dp[cur][j]=max(dp[pre][j-c[i]]+m[i], dp[pre][j])
x=0
while dp[cur][x]<M:
    x+=1
print(x)