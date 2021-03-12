import sys
N,M=map(int, input().split())
cow=[0]
h=[0]*(M+1)
for i in range(N):
    cow.append(list(map(int,sys.stdin.readline().split()[1:])))
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
            return
        h[i]=nx

for i in range(1,N+1):
    cur = [0] * (M + 1)
    check=0
    dfs(i)
print(cnt)