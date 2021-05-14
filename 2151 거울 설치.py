from collections import deque

N = int(input())
mp = [input() for _ in range(N)]
vis = [[[3000] * N for _ in range(N)] for v in range(4)]
# 우하좌상 0123
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

A = []
for i in range(N):
    for j in range(N):
        if mp[i][j] == '#':
            A.append(j)
            A.append(i)
sx = A[0]
sy = A[1]
ex = A[2]
ey = A[3]


def bfs():
    q = deque()
    for i in range(4):
        q.append((sx, sy, i, 0))
    flag = -1
    while q:
        x, y, d, k = q.popleft()
        while 0 <= x < N and 0 <= y < N and mp[y][x] != '*' and vis[d][y][x] > k:
            vis[d][y][x] = k
            if y == ey and x == ex:
                flag = d
                break
            if mp[y][x] == '!':
                vis[(d + 1) % 4][y][x] = k + 1
                vis[(d - 1) % 4][y][x] = k + 1
                q.append((x + dx[(d + 1) % 4], y + dy[(d + 1) % 4], (d + 1) % 4, k + 1))
                q.append((x + dx[(d - 1) % 4], y + dy[(d - 1) % 4], (d - 1) % 4, k + 1))
            x = x + dx[d]
            y = y + dy[d]

        if flag != -1:
            break
    return vis[flag][y][x]


print(bfs())
