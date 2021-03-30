dp=[[0,1,1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1,1,1]]
N=int(input())
k=0
for i in range(N-1):
    k=i%2
    t=(i+1)%2
    for j in range(1,9):
        dp[k][j]=dp[t][j-1]+dp[t][j+1]
    dp[k][0]=dp[t][1]
    dp[k][9]=dp[t][8]
print(sum(dp[k])%1000000000)