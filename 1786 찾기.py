T=input()
P=input()
X=[0]*len(P)

j=0
for i in range(1,len(P)):
    while (j > 0 and P[i] != P[j]):
        j = X[j - 1]
    if P[i]==P[j]:
        j+=1
        X[i] = j
li=[]
j=0
for i in range(len(T)):
    while(j>0 and T[i]!=P[j]):
        j=X[j-1]
    if T[i]==P[j]:
        if j == len(P)-1:
            li.append(i-j+1)
            j = X[j]
        else:
            j+=1

print(len(li))
for i in li:
    print(i, end=' ')