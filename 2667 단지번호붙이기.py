N=int(input())
ma=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for i in range(N):
    ma.append(list(input()))
for i in range(N):
    for j in range(N):
        ma[i][j]=int(ma[i][j])

def sol(ma):
    li=[0,0]
    def dfs(x,y,ma,t,li):
        li[t]+=1
        ma[y][x]=t
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and ma[ny][nx]==1:
                dfs(nx,ny,ma,t,li)

    t=2
    for i in range(N):
        for j in range(N):
            if ma[i][j]==1:
                li.append(0)
                dfs(j,i,ma,t,li)
                t+=1

    li=li[2:]
    li.sort()
    return str(len(li))+'\n'+'\n'.join(map(str,li))
print(sol(ma))

