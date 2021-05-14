N=int(input())
l=[]
for _ in range(N):
    a,b= map(int, input().split())
    l.append((b,a))
l.sort()
cur=l[0][0]
cnt=1
for i in range(1,N):
    if l[i][1]>=cur:
        cnt += 1
        cur = l[i][0]
print(cnt)