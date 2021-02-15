N=int(input())
A=list(map(int,input().split()))
B=[]
C=[]
maxi=0
def find(x, start,end):
    if start==end:
        return start
    mid= (start+end)//2
    if B[mid] >= x:
        return find(x,start,mid)
    else:
        return find(x,mid+1,end)

for i,v in enumerate(A):
    cur=find(v,0,len(B))
    if cur==len(B):
        B.append(v)
        maxi=i
    elif B[cur]>v:
        B[cur]=v
    C.append(cur)

print(len(B))
D=[maxi]
maxv=len(B)-2
for i in range(maxi-1,-1,-1):
    if C[i]==maxv and A[i]<A[maxi]:
        D.append(i)
        maxv-=1
        maxi=i

for i in range(len(D)-1,-1,-1):
    print(A[D[i]],end=' ')