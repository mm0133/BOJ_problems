import sys
import heapq
N, K = map(int, input().split())
je = []
for i in range(N):
    A,B=map(int, sys.stdin.readline().split())
    je.append((A,-B))
bp = []
for i in range(K):
    bp.append(int(sys.stdin.readline()))
bp.sort()
je.sort()
ans=0
h=[]
i=0
for j in range(K):
    while i<N and je[i][0]<=bp[j]:
        heapq.heappush(h, je[i][1])
        i+=1
    if h:
        a=heapq.heappop(h)
        ans+=a
print(-ans)