import sys
N= int(input())
ma=[]
A=list(map(int,sys.stdin.readline().split()))
dp=[A,[0,0,0]]
dp2=[A[:],[0,0,0]]


for i in range(N-1):
    A0, A1, A2 = list(map(int, sys.stdin.readline().split()))
    if i%2:
        dp[0][0] = max(dp[1][0], dp[1][1]) + A0
        dp[0][1] = max(dp[1]) + A1
        dp[0][2] = max(dp[1][1], dp[1][2]) + A2
        dp2[0][0] = min(dp2[1][0], dp2[1][1]) + A0
        dp2[0][1] = min(dp2[1]) + A1
        dp2[0][2] = min(dp2[1][1], dp2[1][2]) + A2

    else:
        dp[1][0] = max(dp[0][0], dp[0][1]) + A0
        dp[1][1] = max(dp[0]) + A1
        dp[1][2] = max(dp[0][1], dp[0][2]) + A2
        dp2[1][0] = min(dp2[0][0], dp2[0][1]) + A0
        dp2[1][1] = min(dp2[0]) + A1
        dp2[1][2] = min(dp2[0][1], dp2[0][2]) + A2

if N%2:
    print(max(dp[0]), min(dp2[0]))
else:
    print(max(dp[1]), min(dp2[1]))
