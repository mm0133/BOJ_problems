from collections import deque

R,C=map(int,input().split())
ma=[]

for i in range(R):
    ma.append(list(input()))

part=[deque([]),deque([]),deque([])]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
ch=0
q=deque([])
def scan(x,y,l,p,op):
    global part,ch,q
    if ch:
        return
    ma[y][x]=p
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<C and 0<=ny<R:
            if ma[ny][nx]=='.' or ma[ny][nx]=='K':
                ma[ny][nx]='S'
                q.append((nx,ny))
            elif ma[ny][nx]=='X':
                ma[ny][nx] = 'V'
                l.append((nx,ny))
            elif ma[ny][nx]=='L' or ma[ny][nx]==op:
                ch=1

def melt(x,y,p,op,vk):
    global li, ch,q
    if ch:
        return
    ma[y][x]=p
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<C and 0<=ny<R:
            if ma[ny][nx]=='X':
                ma[ny][nx]=vk
                li.append((nx,ny))
            elif vk=='V' and  (ma[ny][nx]=='.' or ma[ny][nx]=='K') :
                q.append((nx, ny))
                while q:

                    x, y = q.popleft()
                    scan(x, y, li, p,op)

            elif ma[ny][nx]==op:
                ch=1
                return

c=0
for i in range(R):
    for j in range(C):
        if ma[i][j] == 'L':
            q.append((j,i))
            while q:
                x,y=q.popleft()
                scan(x, y, part[c],c,-1)
            c+=1

for i in range(R):
    for j in range(C):
        if ma[i][j] == 'X':
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if 0 <= nx < C and 0 <= ny < R and ma[ny][nx] == '.':
                    ma[i][j]='K'
                    part[2].append((j, i))
                    break


if ch:
    print(0)
else:
    day=0
    while ch==0:
        li = deque([])
        while part[0]:
            x,y=part[0].popleft()
            melt(x, y, 0, 1,'V')

        part[0]=li
        li = deque([])
        while part[1]:
            x,y=part[1].popleft()
            melt(x, y, 1, 0,'V')

        part[1]=li
        li = deque([])

        while part[2]:
            x,y=part[2].popleft()
            if ma[y][x]=='K':
                melt(x, y, '.', -1,'K')
        part[2]=li
        day+=1

    print(day)


