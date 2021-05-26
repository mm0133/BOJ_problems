import sys

N=int(input())
A=[0]*101
B=[0]*101
for i in range(N):
    a,b= map(int, sys.stdin.readline().split())
    A[a]+=1
    B[b]+=1

    tA=A[:]
    tB=B[:]
    ans=0
    a=0
    b=100
    while(a<=100 and b>=0):
        if A[a]!=0 and B[b]!=0:
            ans = max(ans, a+b)
        if tA[a]==tB[b]:
            a += 1
            b -= 1
        elif tA[a]<tB[b]:
            tB[b]-=tA[a]
            a+=1
        else:
            tA[a] -= tB[b]
            b-=1
    print(ans)