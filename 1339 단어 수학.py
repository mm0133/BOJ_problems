N= int(input())
match={}
X=[{} for i in range(8)]

for i in range(N):
    tem=input()
    l=len(tem)
    for j in range(l):
        if tem[j] in X[l-j-1]:
            X[l-j-1][tem[j]]+=1
        else:
            X[l - j - 1][tem[j]]=1

for i in range(7,-1,-1):
    tem = sorted(X[i].items(),reverse=True,key=lambda item: item[1])
    for j in range(len(tem)):
        if tem[j][0] in match:
            match[tem[j][0]]+=tem[j][1]*(10**i)
        else:
            match[tem[j][0]]=tem[j][1]*(10**i)

tem = sorted(match.items(),reverse=True,key=lambda item: item[1])

ans=0
c=9
for i in range(len(tem)):
    ans+=c*tem[i][1]
    c-=1
print(ans)








