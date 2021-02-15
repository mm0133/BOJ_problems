# N=int(input())
# W=[]
# for i in range(N):
#     W.append(list(map(int, input().split())))
#
# vi=[0]*N
# a=16*1000000
# def dfs(t, x, cost):
#     if x==N-1:
#         if W[t][0]:
#             global a
#             a=min(a,cost+W[t][0])
#         return
#     for i in range(1,N):
#         if W[t][i] and vi[i]==0:
#             vi[i]=1
#             dfs(i,x+1,cost+W[t][i])
#             vi[i] = 0
#
# dfs(0,0,0)
# print(a)
from itertools import count


inf=1000000000
def change(x):
    if x=='0':
        return inf
    else:
        return int(x)
N=int(input())
W=[]
M=1<<N-1
for i in range(N):
    W.append(list(map(change, input().split())))

dp=[[0]*M for i in range(N)]
for i in range(1, N):
    dp[i][0]=W[i][0]
def get(x, A):

    if dp[x][A]!=0:
        return dp[x][A]
    minv=inf
    for i in range(1,N):
        if A & (1<<(i-1)):
            minv=min(minv,W[x][i]+get(i,A & ~(1<<(i-1))))
    dp[x][A]=minv
    return minv
print(get(0,M-1))



