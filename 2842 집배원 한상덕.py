N=int(input())
ma=[]
he=[]

for i in range(N):
    ma.append(input())
for i in range(N):
    he.append(list(map(int, input().split())))
hli=[]
maxv=0
minv=1000001

m=0
for i in range(N):
    for j in range(N):
        if ma[i][j]!='.':
            if ma[i][j]=='P':
                sx=j
                sy=i
            m+=1
            maxv = max(maxv, he[i][j])
            minv = min(minv, he[i][j])
        hli.append(he[i][j])
hli=set(hli)
hli=list(hli)
hli.sort()
dx=[0,1,1,1,0,-1,-1,-1]
dy=[1,1,0,-1,-1,-1,0,1]

cm=0
def dfs(x,y):

    if ma[y][x]!='.':
        global cm
        cm+=1
    vi[y][x]=1
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and vi[ny][nx]==0:
            dfs(nx,ny)


s=hli.index(minv)
e=hli.index(maxv)
ans=10000000
vi=[]

x=0
y=e
xc=0
while x<=s and y<len(hli):

    vi = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if he[i][j] < hli[x] or he[i][j] > hli[y]:
                vi[i][j] = -1
    if vi[sy][sx] == 0:
        cm = 0
        dfs(sx, sy)
        if cm == m:
            ans = min(ans, hli[y] - hli[x])
            x+=1
        else:
            y+=1
    else:
        y+=1
print(ans)


#
# for x in range(s,-1,-1):
#     for y in range(e,len(hli)):
#         if ans<=y-x:
#             continue
#         vi = [[0] * N for _ in range(N)]
#         for i in range(N):
#             for j in range(N):
#                 if he[i][j] < hli[x] or  he[i][j] > hli[y]:
#                     vi[i][j]=-1
#         if vi[sy][sx]==0:
#             cm = 0
#             dfs(sx,sy)
#             if cm==m:
#                 ans=hli[y]-hli[x]
# print(ans)






# start=0
# end=len(hli)
# while start<end:
#     mid = (start + end) // 2
#     vi = [[0] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if he[i][j] > hli[mid]:
#                 vi[i][j]=-1
#     if vi[sy][sx]==0:
#         dfs(sx,sy)
#     if check():
#         end=mid
#     else:
#         start=mid+1
# h=hli[start]
#
# start=0
# end=len(hli)
# while start<end:
#     mid = (start + end) // 2
#     vi = [[0] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if he[i][j] < hli[mid]:
#                 vi[i][j] = -1
#     if vi[sy][sx] == 0:
#         dfs(sx, sy)
#     if check():
#         print(vi)
#         start=mid+1
#     else:
#         end=mid
# l=hli[start-1]
# print(h,l)
# print(h-l)
# maxl=[[0]*N for _ in range(N)]
# minl=[[0]*N for _ in range(N)]
# maxl[sy][sx]=he[sy][sx]
# minl[sy][sx]=he[sy][sx]
# def maxdfs(x,y):
#     for i in range(8):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if 0<=nx<N and 0<=ny<N:
#             tem=maxl[ny][nx]
#             if maxl[ny][nx] == 0:
#                 maxl[ny][nx] = max(he[ny][nx], maxl[y][x])
#             else:
#                 maxl[ny][nx] = max(he[ny][nx], min(maxl[ny][nx], maxl[y][x]))
#             if tem!=maxl[ny][nx]:
#                 maxdfs(nx,ny)
#
#
# def mindfs(x,y):
#     print(minl)
#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < N and 0 <= ny < N:
#             tem = minl[ny][nx]
#             if minl[ny][nx] == 0:
#                 minl[ny][nx] = min(he[ny][nx], minl[y][x])
#             else:
#                 minl[ny][nx] = min(he[ny][nx], max(minl[ny][nx], minl[y][x]))
#             if tem!=minl[ny][nx]:
#                 mindfs(nx,ny)
#
# maxdfs(sx,sy)
# mindfs(sx,sy)
#
# h=0
# l=1000001
# for i in range(N):
#     for j in range(N):
#         if ma[i][j]=='K' or ma[i][j]=='P':
#             h=max(h,maxl[i][j])
#             l=min(l,minl[i][j])
# print(h, l)
# print(minl)

