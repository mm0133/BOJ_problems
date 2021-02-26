import sys
from collections import deque
while True:
    N,M= map(int,input().split())
    if N==0 and M==0:
        break
    edge=[[500002]*N for _ in range(N)]
    S, D = map(int, input().split())
    for i in range(M):
        U,V,P=map(int, sys.stdin.readline().split())
        edge[U][V]=P


    di = [500001] * N
    di[S]=0
    q = deque()
    q.append(S)
    while(q):
        x=q.popleft()
        if x == D:
            continue
        for i in range(N):
            if di[i]>di[x] + edge[x][i]:
                di[i] = di[x] + edge[x][i]
                q.append(i)

    q.append(D)
    while (q):
        x = q.popleft()
        if x==S:
            continue
        for i in range(N):
            if di[x]==di[i]+edge[i][x]:
                edge[i][x]=500002
                q.append(i)

    di = [500001] * N
    di[S] = 0
    q.append(S)
    while (q):
        x = q.popleft()
        if x == D:
            continue
        for i in range(N):
            if di[i] > di[x] + edge[x][i]:
                di[i] = di[x] + edge[x][i]
                q.append(i)
    if di[D]==500001:
        print(-1)
    else:
        print(di[D])