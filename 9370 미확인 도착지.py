#다익스트라
from collections import deque

def solution(adj,s,g,h,hu):
    l=len(adj)
    vi=[-1]*l
    vi[s]=0
    q=deque()
    q.append(s)
    while q:
        cur=q.pop()
        for p in adj[cur]:
            if vi[p]==-1:
                vi[p]=adj[cur][p]+vi[cur]
                q.append(p)
            elif adj[cur][p] + vi[cur]<vi[p]:
                vi[p]=adj[cur][p] + vi[cur]
                q.append(p)
    if vi[g]<vi[h]:
        x=h
    else:
        x=g

    vix = [-1] * l
    vix[x] = 0
    q = deque()
    q.append(x)
    while q:
        cur = q.popleft()
        for p in adj[cur]:
            if vix[p] == -1:
                vix[p] = adj[cur][p] + vix[cur]
                q.append(p)
            elif adj[cur][p] + vix[cur] < vix[p]:
                vix[p] = adj[cur][p] + vix[cur]
                q.append(p)
    ans=[]
    for h in hu:
        if vix[h]+vi[x]==vi[h]:
            ans.append(h)
    ans.sort()
    return ans


T=int(input())
for _ in range(T):
    n,m,t=map(int, input().split())
    s,g,h=map(int, input().split())
    adj=[{} for _ in range(n+1)]
    for i in range(m):
        a, b, d=map(int, input().split())
        adj[a][b]=d
        adj[b][a]=d
    hu=[]
    for i in range(t):
        hu.append(int(input()))

    answer=''
    for i in solution(adj,s,g,h,hu):
        answer+=str(i)+' '
    print(answer)
