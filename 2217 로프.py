import sys

N=int(input())
A=[]
for i in range(N):
    A.append(int(sys.stdin.readline()))
A.sort(reverse=True)
i=1
w=A[0]
for i in range(1,N):
    if w<(i+1)*A[i]:
        w = (i + 1) * A[i]
print(w)

