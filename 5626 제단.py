N=int(input())
dp=[]
li=list(map(int,input().split()))
c=1
for i in range(len(li)):
    if i <= N // 2:
        if li[i] > i + 1:
            c = 0
            break
    else:
        if (N - i) < li[i]:
            c = 0
            break
    if li[0]>0:
        c=0
        break
leng=(((N+1)//2)+2)
dp.append([0]*(leng+1))
dp.append([0]*(leng+1))

dp[0][1]=1
if c:
    for p in range(1,N):
        i=p%2
        j=(p+1)%2
        if li[p]!=-1:

            for l in range(len(dp[i])):
                dp[i][l]=0
            dp[i][li[p]+1]=dp[j][li[p]]+dp[j][li[p]+1]+dp[j][li[p]+2]
            dp[i][li[p]+1]%=1000000007
            if dp[i][li[p]+1]==0:
                c=0
                break
        else:
            k=1
            while True:
                if p<=N//2:
                    if k>p+1:
                        break
                else:
                    if (N-p)<k:
                        break
                dp[i][k]=dp[j][k]+dp[j][k-1]+dp[j][k+1]
                dp[i][k]%=1000000007
                k += 1
            while k<leng:
                dp[i][k]=0
                k+=1
if c:
    print(dp[(N-1)%2][1])
else:
    print(0)
