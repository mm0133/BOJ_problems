#세그먼트트리
N=int(input())
A=input().split()
B=input().split()
Bdic={}
for i,v in enumerate(B):
    Bdic[v]=i

tree=[0]*(1<<20)
c=1<<19

def put(x):
    cur = c + x
    while cur:
        tree[cur]+=1
        cur = cur >> 1

def find(x):
    order=0
    cur=1
    boundary=c>>1
    move=c>>2

    while True:
        cur = (cur << 1) +1
        if x<boundary:
            order += tree[cur]
            cur -= 1
            boundary-=move
        else:
            boundary+=move
        if move==0:
            break
        move=move>>1
    return order
ans=0
for a in A:
    x=Bdic[a]
    put(x)
    ans+=find(x)
print(ans)
