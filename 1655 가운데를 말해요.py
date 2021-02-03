# sys.stdin.readline() 가 input보다 훨빠름 input써서 시간초과남
# center를 기준으로 왼쪽에 maxh 오른쪽에minh을 줬는데
# 생각해보면 maxh의 top을 center로 생각해서 짰으면 center 생략가능

#maxheap 초기화 할때 음수값 넣어서 초기화하는거 까먹지말기
#처음 시작할때 input 세번 지저분하게 하지말고  maxh 랑 minh에 최댓값 최솟값 박아놓으면 훨씬 간단하게 예외처리가능
import sys
import heapq
N=int(input())
center=int(sys.stdin.readline())
print(center)
lt=int(sys.stdin.readline())
if center <lt:
    center, lt = lt, center
print(lt)
rt=int(sys.stdin.readline())
if rt<center:
    rt, center=center,rt
    if center<lt:
        center, lt = lt, center
print(center)


maxh=[-lt] #왼쪽)
minh=[rt] #오른쪽


op=False #오른쪽이 하나 많을때 True

for i in range(N-3):
    tem=int(sys.stdin.readline())
    if op:
        if tem>center:
            heapq.heappush(maxh, -center)
            if tem > minh[0]:
                center=heapq.heappop(minh)
                heapq.heappush(minh,tem)
            else:
                center=tem
        else:
            heapq.heappush(maxh, -tem)
        op=False
    else:
        if tem < center:
            heapq.heappush(minh, center)
            if tem < -maxh[0]:
                center=-heapq.heappop(maxh)
                heapq.heappush(maxh,-tem)
            else:
                center=tem
        else:
            heapq.heappush(minh, tem)
        op = True
    print(center)