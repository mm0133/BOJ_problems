while True:
    N, A, B = map(int, input().split())
    if N == 0 and A==0 and B==0:
        break
    disA = []
    disB = []
    num = []
    rank = []
    for i in range(N):
        n, a, b = map(int, input().split())
        disA.append(a)
        disB.append(b)
        num.append(n)
        rank.append((a - b, i))
    rank.sort()
    sm = 0
    ka = 0
    while A > 0 and rank[ka][0] <= 0 and ka<N: #ka<N 도 까먹지말자
        cur=rank[ka][1]
        if A - num[cur] >= 0:
            A -= num[cur]
            sm += num[cur] * disA[cur]
            ka += 1
        else:
            num[cur] -= A
            sm += A * disA[cur]
            A = 0
    kb = N - 1
    while B > 0 and rank[kb][0] >= 0 and kb>=ka: # kb>=ka 이조건 못찾아서 개고생함 ㅜ
        cur = rank[kb][1]
        if B - num[cur] >= 0:
            B -= num[cur]
            sm += num[cur] * disB[cur]
            kb -= 1
        else:
            num[cur] -= B
            sm += B * disB[cur]
            B = 0
    if B!=0:
        for i in range(ka, kb + 1):
            sm += num[rank[i][1]] * disB[rank[i][1]]
    else:
        for i in range(ka, kb + 1):
            sm += num[rank[i][1]] * disA[rank[i][1]]


    print(sm)
