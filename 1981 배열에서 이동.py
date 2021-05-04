import sys
sys.setrecursionlimit(100000)
N= int(input())
mp=[]
for i in range(N):
    mp.append(list(map(int,input().split())))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(x,y,s,e):
    vi[y][x]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and s<=mp[ny][nx]<=e and vi[ny][nx]==0:
            dfs(nx,ny,s,e)
s=0
ch=0
e=max(mp[0][0],mp[N-1][N-1])
m=min(mp[0][0],mp[N-1][N-1])
while e<=200 and s<=m:
    vi = [[0] * N for _ in range(N)]
    dfs(0,0,s,e)
    if vi[N-1][N-1]:
        s+=1
        ch=1
    elif ch:
        e+=1
        s+=1
    else:
        e+=1
print(e-s+1)