import time

start = time.time()

X=[1,1,3,3,2,3,2,2]
X=set(X)
X=list(X)
# print(X)
A=[(1,2),(1,4),(1,3),(2,2)]
A.sort(key=lambda x: x[0])
print(A)
A=[0,0,0]

l=0
r=len(A)
while l != r:
    m=(l+r)//2
    if A[m]==1:
        r=m
    else:
        l=m+1
print(l)
print(r)
# print("time :", time.time() - start)  #
