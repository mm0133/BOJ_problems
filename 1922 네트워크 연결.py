# import sys
# sys.setrecursionlimit(100000)
# #
# N=int(input())
# M=int(input())
# cost=[]
# for i in range(M):
#     A=list(map(int, input().split()))
#     if A[0]==A[1]:
#         continue
#     A[0]-=1
#     A[1]-=1
#     cost.append(A)
# cnt=0
# ans=100000000
# u=1
#
# vi=[0]*N
# visited=[0]*len(cost)
#
# def dfs(x,c):
#     global u,cnt
#
#     if cnt==N-1:
#         global ans
#         if vi[0]!=0:
#             for i in vi:
#                 if i!=vi[0]:
#                     return
#         else:
#             return
#         ans=min(ans,c)
#         return
#     if x==M:
#         return
#
#     if not(vi[cost[x][0]] or vi[cost[x][1]]):
#
#
#         visited[x]=1
#         vi[cost[x][0]]=u
#         vi[cost[x][1]]=u
#         u += 1
#         cnt+=1
#         dfs(x+1, c+cost[x][2])
#         visited[x]=0
#         vi[cost[x][0]] = 0
#         vi[cost[x][1]] = 0
#         u-=1
#         cnt-=1
#
#     elif vi[cost[x][0]] and not(vi[cost[x][1]]):
#         visited[x]=1
#         vi[cost[x][1]]=vi[cost[x][0]]
#         cnt+=1
#         dfs(x+1, c+cost[x][2])
#         cnt-=1
#         visited[x]=0
#         vi[cost[x][1]]=0
#     elif not(vi[cost[x][0]]) and vi[cost[x][1]]:
#         visited[x] = 1
#         vi[cost[x][0]]=vi[cost[x][1]]
#         cnt+=1
#         dfs(x+1, c+cost[x][2])
#         cnt-=1
#         visited[x]=0
#         vi[cost[x][0]] = 0
#     elif vi[cost[x][0]] != vi[cost[x][1]]:
#         tem = vi[cost[x][1]]
#         temli = []
#         visited[x] = 1
#         for i, v in enumerate(vi):
#             if v == tem:
#                 vi[i] = vi[cost[x][0]]
#                 temli.append(i)
#         cnt += 1
#         dfs(x + 1, c + cost[x][2])
#         cnt -= 1
#         visited[x] = 0
#         for i in temli:
#             vi[i] = tem
#     if len(visited)-x >  N-1-cnt:
#         dfs(x + 1, c)
#
# dfs(0,0)
# print(ans)


## 크루스칼 알고리즘 배움
## 위는 크루스칼알고리즘을 적용하지 않아 가중치를 정렬하지 않고 주어진 경로를 2^M으로 완전탐색함(시간복잡도 어마어마)
## union find 구현할 때 필요할때만 업데이트 하면 되는데 union시 부모의 부모가 생기면 그자식들의 부모도 전부 갱신해서 오래걸림

N=int(input())
M=int(input())

cost=[]
for i in range(M):

    A=list(map(int, input().split()))
    if A[0]==A[1]:
        continue
    A[0]-=1
    A[1]-=1
    cost.append(A)
cnt=0
c=0
i=0
u=1
union={}
vi=[0]*N

cost.sort(key=lambda x : x[2])
while cnt<N-1:
    if not (vi[cost[i][0]] or vi[cost[i][1]]):
        union[u]=[cost[i][0],cost[i][1]]
        vi[cost[i][0]]=u
        vi[cost[i][1]]=u
        u+=1
        cnt += 1
        c+=cost[i][2]
    elif vi[cost[i][0]]and not(vi[cost[i][1]]):
        union[vi[cost[i][0]]].append(cost[i][1])
        vi[cost[i][1]] = vi[cost[i][0]]
        cnt += 1
        c += cost[i][2]
    elif not(vi[cost[i][0]]) and vi[cost[i][1]]:
        union[vi[cost[i][1]]].append(cost[i][0])
        vi[cost[i][0]] = vi[cost[i][1]]
        cnt += 1
        c += cost[i][2]
    elif vi[cost[i][0]] != vi[cost[i][1]]:
        cnt+=1
        c+=cost[i][2]
        if len(union[vi[cost[i][0]]])<len(union[vi[cost[i][1]]]):
            tem=vi[cost[i][0]]
            for j in union[tem]:
                vi[j] = vi[cost[i][1]]
            union[vi[cost[i][1]]]+=union[tem]
            union.pop(tem)
        else:
            tem = vi[cost[i][1]]
            for j in union[tem]:
                vi[j] = vi[cost[i][0]]
            union[vi[cost[i][0]]] += union[tem]
            union.pop(tem)
    i+=1

print(c)