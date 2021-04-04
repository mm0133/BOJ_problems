from itertools import combinations
N=int(input())
ma=[]
ts=[]
combi=[]
for i in range(N):
    ma.append(input().split())
for i in range(N):
    for j in range(N):
        if ma[i][j]=='T':
            ts.append((j,i))
        elif ma[i][j]=='X':
            combi.append(i*N+j)

P = combinations(combi,3)
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def laser(x,y,dir):
    nx=x+dx[dir]
    ny=y+dy[dir]
    if 0 <= nx < N and 0 <= ny < N :
        if ma[ny][nx] == 'X':
            return laser(nx, ny, dir)
        elif ma[ny][nx] =='S':
            return 1
    return 0

ans="NO"
b=0
for p in P:
    for o in p:
        ma[o//N][o%N]='O'
    ch=0
    for t in ts:
        for i in range(4):
            if laser(t[0], t[1], i)==1:
                ch=1
                break

    if ch ==0:
        ans="YES"
        break
    for o in p:
        ma[o//N][o%N]='X'
print(ans)