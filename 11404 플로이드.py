n=int(input())
m=int(input())
dis=[[10000001]*(n+1) for i in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    dis[a][b]=min(dis[a][b],c)
for i in range(n+1):
    dis[i][i]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])

def tr(x):
    if x==10000001:
        return '0'
    return str(x)

for i in range(1, n+1):
    print(" ".join(map(tr,dis[i][1:])))
