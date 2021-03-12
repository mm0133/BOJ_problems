import sys
N,M =map(int,input().split())
R=0
li=[]
for i in range(N):
    a,b=map(int, sys.stdin.readline().split())
    if a>b:
        li.append((b,a))
li.sort()
start=li[0][0]
end=li[0][1]
ans=0
for i in li:
    if i[0]<=end:
        if i[1]>end:
            end=i[1]
    else:
        ans+=end-start
        start = i[0]
        end = i[1]
ans+=end-start
print(2*ans +M)