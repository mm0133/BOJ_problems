import time

start = time.time()

X=[1,1,3,3,2,3,2,2]
X=set(X)
X=list(X)
# print(X)

A=[0,0,1]
a,b,c=A
print(a,b,c)
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
