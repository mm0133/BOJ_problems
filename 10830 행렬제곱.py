from copy import deepcopy

N,B=map(int,input().split())
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))
dp=[0]*40
for i in range(N):
    for j in range(N):
        A[i][j] = A[i][j] % 1000
dp[0]=A

def mul(A1,A2):
    A3=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tem=0
            for k in range(N):
                tem+=A1[i][k]*A2[k][j]
            A3[i][j]=tem%1000
    return A3

def getAn(x):
    if dp[x]==0:
        dp[x]= mul(getAn(x-1),getAn(x-1))
    return dp[x]
x=1
i=0
ans=[[0]*N for i in range(N)]
ch=0
while x<=B:
    if x & B:
        if ch:
            ans=mul(getAn(i),ans)
        else:
            ans=getAn(i)
            ch=1
    x=x<<1
    i+=1

for i in range(N):
    s = ''
    for j in range(N):
        s=s+str(ans[i][j])+' '
    print(s)
