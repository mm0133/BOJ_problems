N, K = map(int, input().split())
W=[]
V=[]
for i in range(N):
    A,B=map(int, input().split())
    W.append(A)
    V.append(B)

dp=[[0]*(K+1) for i in range(N)]
c=0

if W[0]<K+1:
    for i in range(W[0],K+1):
        dp[0][i]=V[0]

for i in range(1,N):
    for j in range(K+1):
        pr=j - W[i]
        if pr>=0:
            dp[i][j]=max(dp[i-1][pr]+V[i],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])

