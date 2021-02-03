# 코드에서 시간 단축할부분: dis가 중복 계산되므로 이것도 dp로 저장해놓고 불러오기
# 차순서 구하려고 뒤로 다시 돌아갈때  앞에서 dp[col][col-1]이 어디서 온건지 전부 저장해놓았으면
# 돌아갈때 row찾는 반복을 안해도 되서 시간이줄듯
# mv=2*W*M 이 자주호출되므로 이것도 저장해놓고쓰기

N=int(input())
W=int(input())
wl=[[1,1],[N,N]]
for i in range(W):
    wl.append(list(map(int,input().split())))

def dis(x,y):
    return abs(wl[x][0]-wl[y][0])+abs(wl[x][1] - wl[y][1])

dp=[[0]*(W+2) for i in range(W+2)]
car=[[-1]*(W+2) for i in range(W+2)]
car[1][0]=1 # 0 1

# 각루트마다 차와 거리최솟값을 dp로 저장
#dp[i][j]는 i-2번째 명령이 실행되고(마지막움직인차는 여기 위치)  나머지차가 j-2번째 명령위치에 있음을 나타냄
# 명령에 맨처음의 0,0  N,N을 추가해 +2 의 오프셋이 생김
for i in range(2,W+2):
    mv = 2 * N * W
    for j in range(i-1):
        dp[i][j]=dp[i-1][j]+dis(i,i-1)
        car[i][j]=car[i-1][j]
        if mv>dp[i-1][j]+dis(i,j):
            mv=dp[i-1][j]+dis(i,j)
            car[i][i-1]=(car[i-1][j]+1)%2
    dp[i][i-1]=mv

#거리최솟값은 마지막행의 원소중 최솟값, 그리고 그위치의 row좌표를 구함
mv = 2 * N * W
for i in range(W+1):
    if mv>dp[W+1][i]:
        mv=dp[W+1][i]
        r=i
c=W+1

print(mv)

#역추적하면서 차의 호출순서를 리스트에담음
li=[(c,r)]
while 2<c:

    if r==c-1:
        for j in range(c-1):
            if dp[c - 1][j] + dis(c, j) == dp[c][r]:
                r=j
                break
    c-=1
    li.append((c, r))
#역으로 담긴리스트를 거꾸로 출력함.
for i in range(W-1,-1,-1):
    print((car[li[i][0]][li[i][1]]+1))