N,M=map(int,input().split())
ma=[]
for i in range(N):
    ma.append(list(map(int,input().split())))
dx=[0,1,0,-1]
dy=[1,0,-1,0]

# 맵을 스캔하고 섬을 구분짓는다. 각섬의 모든 위치를 배열에 저장한다.
def scan(x,y,li,t):
    ma[y][x]=t
    li.append((x,y))
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<M and 0<=ny<N and ma[ny][nx]==1:
            scan(nx,ny,li,t)

islands=[]
ct=2
for i in range(N):
    for j in range(M):
        if ma[i][j]==1:
            li=[]
            scan(j,i,li,ct)
            islands.append(li)
            ct+=1

#각섬마다 거리를 인접 행렬로 만든다.
adj=[[101]*len(islands) for _ in range(len(islands))]
def laser(x,y,t,dir,l):
    nx=x+dx[dir]
    ny=y+dy[dir]
    if 0 <= nx < M and 0 <= ny < N :
        if ma[ny][nx] == 0:
            laser(nx, ny, t, dir, l+1)
        elif ma[ny][nx] != t and l>1:
            adj[t-2][ma[ny][nx]-2]=min(adj[t-2][ma[ny][nx]-2],l)

for island in islands:
    for spot in island:
        for i in range(4):
            laser(spot[0],spot[1],ma[spot[1]][spot[0]],i,0)


#인접행렬의 요소들을 비용오름차순으로 정렬한 후 크루스칼알고리즘을 적용
cost=[]
for i in range(len(adj)):
    for j in range(i+1,len(adj)):
        if adj[i][j]<101:
            cost.append((i,j,adj[i][j]))
cost.sort(key=lambda x:x[2])

p=[]
for i in range(len(adj)):
    p.append(i)

def find(x):
    if x!=p[x]:
        p[x]=find(p[x])
    return p[x]

def union(u,v):
    root1= find(u)
    root2=find(v)
    p[root2]=root1

c=0
cur=0
ans=0
while c<len(adj)-1:
    if cur==len(cost):
        ans=-1
        break
    u,v, wt= cost[cur]

    if find(u)!= find(v):
        union(u,v)
        ans+=wt
        c+=1
    cur += 1
print(ans)


