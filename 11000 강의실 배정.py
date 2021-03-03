N=int(input())
A=[]

for i in range(N):
    a,b=map(int, input().split())
    A.append((a,1))
    A.append((b,0))
A.sort()
v=0
c=0
for i in A:
    if i[1]:
        c+=1
        v=max(c,v)
    else:
        c-=1
print(v)



