import sys
G=int(sys.stdin.readline())
P=int(sys.stdin.readline())
gp=[i for i in range(G+1)]
def find(x):
    if gp[x]!=x:
        gp[x]=find(gp[x])
    return gp[x]
cnt=0
for j in range(P):
    gi=int(sys.stdin.readline())
    cur = find(gi)
    if cur == 0:
        break
    gp[cur] = find(cur - 1)
    cnt+=1
print(cnt)
