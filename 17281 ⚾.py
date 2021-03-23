import sys
from itertools import permutations
A=permutations([1,2,3,4,5,6,7,8],8)
N=int(input())
bo=[]
for i in range(N):
    bo.append(list(map(int,sys.stdin.readline().split())))
max_score=0
for p in A:
    out=0
    score=0
    k=0
    i=0
#리스트 형태로 run=[0,0,0]으로 선언하면 참조하는 시간때문에 시간초과 났음
    r0,r1,r2=0,0,0

    # while i<N:
    #     if k==3:
    #         j=0
    #     elif k<3:
    #         j=p[k]
    #     else:
    #         j = p[k - 1]
    #아래가 조금더 빠름 if 문 반복이 안되서 그런듯
    order=p[:3]+(0,)+p[3:]
    while i<N:
        j=order[k]
        if bo[i][j]==0:
            if out==2:
                out=0
                i+=1
                r0,r1,r2=0,0,0
            else:
                out += 1
        elif bo[i][j]==1:
            score+=r2
            r0,r1,r2 =1,r0,r1
        elif bo[i][j]==2:
            score+=r1+r2
            r0,r1,r2 = 0, 1, r0
        elif bo[i][j]==3:
            score+=r0+r1+r2
            r0,r1,r2=0,0,1
        else:
            score+=r0+r1+r2+1
            r0,r1,r2=0,0,0
        if k==8:
            k=0
        else:
            k+=1
    if score>max_score:
        max_score=score
print(max_score)
