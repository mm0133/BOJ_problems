N=int(input());A=[];v=0;c=0;
for i in range(N):a,b=map(int, input().split());A.extend([(a,1),(b,0)])
A.sort()
for i in A:
 if i[1]:c+=1;v=max(c,v)
 else:c-=1
print(v)
