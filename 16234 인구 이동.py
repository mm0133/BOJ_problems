import sys
sys.setrecursionlimit(2500)
N,L,R=map(int,input().split())
ma=[]
for i in range(N):
    ma.append(list(map(int,input().split())))
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def sol(ma):

    ans=0
    def dfs(x,y,ma,t,su,cnt):
        su[t]+=ma[y][x]
        cnt[t]+=1
        vi[y][x]=t
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and vi[ny][nx]==-1 and L<=abs(ma[y][x]-ma[ny][nx])<=R:
                dfs(nx,ny,ma,t,su,cnt)

    while True:
        vi = [[-1] * N for _ in range(N)]
        su = []
        cnt = []
        t=0
        for i in range(N):
            for j in range(N):
                if vi[i][j]==-1:
                    su.append(0)
                    cnt.append(0)
                    dfs(j,i,ma,t,su,cnt)
                    t+=1
        if len(su)==N*N:
            break
        ans+=1
        for i in range(len(su)):
            su[i]=su[i]//cnt[i]
        for i in range(N):
            for j in range(N):
                ma[i][j]=su[vi[i][j]]

    return ans
print(sol(ma))