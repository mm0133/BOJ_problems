N=int(input())
i=0
li=[]
for i in range(N):
    x,y=map(int,input().split())
    if x>y:
        x,y=y,x
    li.append((x,y))
li.sort()

start=li[0][0]
end=li[0][1]
ans=0
for i in range(N):
    if start<=li[i][0]<=end:
        if li[i][1]>end:
            end=li[i][1]
    else:
        ans+=end-start
        start = li[i][0]
        end = li[i][1]
ans+=end-start
print(ans)