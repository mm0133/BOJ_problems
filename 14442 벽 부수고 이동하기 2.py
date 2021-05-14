from collections import deque

N,M,K = map(int, input().split())
mp=[input() for _ in range(N)]
vis=[ [ [-1]*M for v in range(N)] for _ in range(K+1)]
vis[0][0][0]=1
dy=[1,-1,0,0]
dx=[0,0,1,-1]

def bfs():
    q=deque()
    q.append((0,0,0))
    while(q):
        x,y,k=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<M and 0<=ny<N:

                if mp[ny][nx]=='1':
                    if  k<K:
                        if vis[k+1][ny][nx]==-1:
                            vis[k+1][ny][nx]=vis[k][y][x]+1
                            q.append((nx, ny, k + 1))
                else:
                    if vis[k][ny][nx]==-1:
                        vis[k][ny][nx]=vis[k][y][x]+1
                        q.append((nx, ny, k))

    answer=1000001
    for i in range(K+1):
        if vis[i][N-1][M-1]!=-1 and answer>vis[i][N-1][M-1]:
            answer=vis[i][N-1][M-1]
    if answer==1000001:
        answer=-1
    return answer

print(bfs())
