from math import ceil


def go(maxhp):
    hp = maxhp
    curatk = atk
    for t, a, h in stage:
        if t == 1:
            num_atk=ceil(h/curatk)
            if num_atk>ceil(hp/a):
                return 0
            else:
                hp-=(num_atk-1)*a

        else:
            curatk += a
            hp = min(maxhp, hp + h)
    return 1

N,atk=map(int,input().split())
stage=[list(map(int,input().split())) for _ in range(N)]
r=123456*1000000*1000000
l=1

while r!=l:
    m=(r+l)//2
    if go(m):
        r=m
    else:
        l=m+1
print(r)