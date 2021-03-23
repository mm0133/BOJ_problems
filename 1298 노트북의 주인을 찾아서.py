import sys
N,M=map(int, input().split())
cow=[[] for i in range(N+1)]
h=[0]*(N+1)
for i in range(M):
    A,B=map(int,sys.stdin.readline().split())
    cow[A].append(B)
cnt=0
def dfs(x):
    global check, cnt
    for i in cow[x]:
        if h[i]==0:
            h[i]=x
            check=1
            cnt+=1
            return
    for i in cow[x]:
        if cur[i]:
            continue
        nx=h[i]
        h[i]=x
        cur[i] = 1
        dfs(nx)
        if check:
            cur[i] = 0
            return
        h[i]=nx
cur = [0] * (N + 1)
for i in range(1,N+1):

    check=0
    dfs(i)
print(cnt)