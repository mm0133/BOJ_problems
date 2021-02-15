import sys

while True:
    W, H = map(int, sys.stdin.readline().split())
    if W == 0 and H == 0:
        break
    #묘지 위치표시
    G = int(sys.stdin.readline())
    Gl = [[0] * W for i in range(H)]
    for i in range(G):
        tem=list(map(int, sys.stdin.readline().split()))
        Gl[tem[1]][tem[0]]=1
    #귀신구멍 위치표시+ 귀신구멍 순간이동 엣지 추가
    E = int(sys.stdin.readline())
    El = [[0] * W for i in range(H)]
    edge=[]
    for i in range(E):
        tem = list(map(int, sys.stdin.readline().split()))
        if tem[0]==W and tem[1]==H:
            continue
        edge.append(tem)
        El[tem[1]][tem[0]] = 1


    #잔디일때 엣지추가 , 도착점일때 제외
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for j in range(H):
        for k in range(W):
            if (k == W - 1 and j == H - 1) or Gl[j][k] or El[j][k]:
                continue
            for l in range(4):
                nx = k + dx[l]
                ny = j + dy[l]
                if 0 <= nx < W and 0 <= ny < H and Gl[ny][nx]==0:
                    edge.append([k,j,nx,ny,1])


    inf = 1000000000000
    ma = [[inf] * W for i in range(H)]
    ma[0][0]=0
    #엣지를 돌면서 relax
    #ma[j[1]][j[0]] < inf 가 없어서 너무 고생했다.. ㅠㅠㅠ 도달할수없는 곳에서
    # 귀신구멍중 음수값을 갖는 친구가 inf값을 줄일수있기때문에 impossible 케이스에서 오류가 났다.
    for i in range(W*H-1):
        for j in edge:
            if ma[j[1]][j[0]] < inf and ma[j[1]][j[0]]+j[4]<ma[j[3]][j[2]] :
                ma[j[3]][j[2]]=ma[j[1]][j[0]]+j[4]
    never = 0
    #음수싸이클 확인
    for j in edge:
        if ma[j[1]][j[0]] < inf and ma[j[1]][j[0]] + j[4] < ma[j[3]][j[2]]:
            never=1
            break

    if never:
        print('Never')
    elif ma[H - 1][W - 1] == inf:
        print('Impossible')
    else:
        print(ma[H - 1][W - 1])

