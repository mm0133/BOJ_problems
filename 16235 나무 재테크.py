N, M, K=map(int,input().split())
A=[]
namu=[]
Y=[[5]*N for _ in range(N)]
for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(N):
    namu.append([])
    for j in range(N):
        namu[i].append([])
for i in range(M):
    x,y,z= map(int, input().split())
    namu[x-1][y-1].append(z)
for i in range(N):
    for j in range(N):
        namu[i][j].sort()

dy=[1,1,1,0,-1,-1,-1,0]
dx=[-1,0,1,1,-1,0,1,-1]



for _ in range(K):
    #봄여름
    for i in range(N):
        for j in range(N):
            cur=namu[i][j]
            s=len(cur)
            for k in range(len(cur)):
                if Y[i][j]>=cur[k]:
                    Y[i][j]-=cur[k]
                    cur[k]+=1
                else:
                    s=k
                    break
            for k in range(s,len(cur)):
                Y[i][j]+=cur[k]//2
            namu[i][j]=cur[:s]
    #가을 겨울
    tem=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cur = namu[i][j]
            for k in range(len(cur)):
                if cur[k]%5==0:
                    for l in range(8):
                        nx=j+dx[l]
                        ny=i+dy[l]
                        if 0<=nx<N and 0<=ny<N:
                            tem[ny][nx]+=1
    for i in range(N):
        for j in range(N):
            namu[i][j]=[1]*tem[i][j]+namu[i][j]
            Y[i][j]+=A[i][j]

ans=0
for i in range(N):
    for j in range(N):
        ans+=len(namu[i][j])

print(ans)