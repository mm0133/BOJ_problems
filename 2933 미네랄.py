R,C=map(int , input().split())
ma=[]
for i in range(R):
    X=input()
    tem=[]
    for j in range(C):
        tem.append(X[j])
    ma.append(tem)


dx=[1,0,-1,0]
dy=[0,1,0,-1]
def crush(x,y):
    ma[y][x]='.'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and ma[ny][nx]=='x':
            cma = [[0] * C for _ in range(R)]
            if check(nx, ny, cma)==0:
                fall(cma)
                break
def check(x,y,cma):
    cma[y][x]=1
    if y==R-1:
        return 1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<C and 0<=ny<R and ma[ny][nx]=='x' and cma[ny][nx]==0:
            if check(nx,ny,cma):
                return 1
    return 0

def fall(fma):

    w=[-1]*C
    for j in range(C):
        for i in range(R-1,-1,-1):
            if fma[i][j]:
                w[j]=i
                break
    fh=2
    stop=0
    while True:
        for j in range(C):
            if w[j]==-1:
                continue
            if w[j]+fh>=R or ma[w[j]+fh][j]=='x':
                stop=1
                break
        if stop:
            fh-=1
            break
        fh+=1
    for i in range(R-1,-1,-1):
        for j in range(C):
            if fma[i][j]:
                ma[i][j]='.'
                ma[i+fh][j]='x'

N=int(input())
left=True
for i in map(int,input().split()):
    h=R-i
    x=-1
    if left:
        for j in range(C):
            if ma[h][j]=='x':
                x=j
                break
    else:
        for j in range(C-1,-1,-1):
            if ma[h][j]=='x':
                x=j
                break
    if x!=-1:
        crush(x,h)
    left = not left

for i in range(R):
    print(''.join(ma[i]))