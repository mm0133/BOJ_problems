N,M=map(int,input().split())
d=[(1,1),(1,-1),(-1,1),(-1,-1)]
ma=[list(map(int, input().split())) for _ in range(N)]
vis=[[0]*M for _ in range(N)]
answer=0
def backtrack(x,y,k):
    if y==N:
        global answer
        answer=max(answer,k)
        return
    ty = y + (x+1) // M
    tx = (x + 1) % (M)
    if vis[y][x]==0:
        for i in range(4):
            nx=x+d[i][0]
            ny=y+d[i][1]
            if 0<=nx<M and 0<=ny<N and vis[ny][x]==0 and vis[y][nx]==0:
                vis[y][x]=1
                vis[ny][x]=1
                vis[y][nx]=1
                backtrack(tx, ty, k+2*ma[y][x]+ma[ny][x]+ma[y][nx])
                vis[y][x] = 0
                vis[ny][x] = 0
                vis[y][nx] = 0
    backtrack(tx, ty, k)

backtrack(0,0,0)
print(answer)