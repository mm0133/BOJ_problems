dp=[[0]*101 for _ in range(101)]
combi=[[0]*101 for _ in range(101)]
fct=[0]*101
fct[0]=1
fct[1]=1

def factorial(k):
    if fct[k]==0:
        fct[k]=factorial(k-1)*k
    return fct[k]
def getCombi(x,y):
    if combi[x][y]==0:
        combi[x][y]=factorial(x)//factorial(x-y)//factorial(y)
    return combi[x][y]

for i in range(1,101):
    dp[i][i]=1
    dp[i][0]=1
    dp[i][1]=factorial(i-1)


def get(n,m):
    if dp[n][m]==0:
        for i in range(m-1,n):
            dp[n][m]+= getCombi(n-1,i)*get(i,m-1)*factorial(n-i-1)
    return dp[n][m]


N,L,R=map(int, input().split())

ans=0
if L==1 and R==1:
    if N==1:
        ans=1
    else:
        ans=0
elif R==1 or L==1:
    ans = get(N - 1, R*L-1)
else:
    for i in range(N-1):
        ans+=get(i,L-1)*get(N-i-1,R-1)*getCombi(N-1,i)
print(ans%1000000007)

# dp[5][1][0]=(4C0)*dp[1][0]*4!
# dp[5][1][1]=0
# dp[5][1][2]=0
# dp[5][1][3]=0
# dp[5][1][4]=0
#
# dp[5][2][0]=0
# dp[5][2][1]=(4C1)*dp[1][1]*(3!)
# dp[5][2][2]=(4C2)*dp[2][1]*(2!)
# dp[5][2][3]=(4C3)*dp[3][1]*1!
# dp[5][2][4]=(4C4)*dp[4][1]*0!
#
# dp[5][3][0]=0
# dp[5][3][1]=0
# dp[5][3][2]=(4C2)*dp[2][2]*2!
# dp[5][3][3]=(4C3)*dp[3][2]*1!
# dp[5][3][4]=(4C4)*dp[4][2]*0!
#
# dp[5][4][0]=0
# dp[5][4][1]=0
# dp[5][4][2]=0
# dp[5][4][3]=4C3*dp[3][3]1!
# dp[5][4][4]=4C4*dp[4][3]0!


