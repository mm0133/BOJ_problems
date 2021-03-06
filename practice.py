import sys
from itertools import combinations

N = int(sys.stdin.readline())
M = []
for i in range(N):
    M.append(sys.stdin.readline().split())


# T 위치 -> 상하좌우 탐색 : s 만나면 멈추고 장애물 1 설치 만약 겹치는 부분이 존재한다면 장애물위치를 그걸로 옮기고원래 두개 하나로 갯수 합치기
# s위치 -> 상파좌우 탐색 : t만나면 멈추고 장애물 설치 
dy=[0,1,0,-1]
dx=[1,0,-1,0]

def findS():
    for teacher in teachers:
        x, y = teacher
        for k in range(4):
            nx = y
            ny = x
            while 1:
                ny+=dy[k]
                nx+=dx[k]
                if ny < 0 or ny >= N or nx < 0 or nx >= N or M[ny][nx] == 'B':
                    break
                if M[ny][nx] == 'S':
                    return False
    return True


empty = []
teachers = []
for i in range(N):
    for j in range(N):
        if M[i][j] == 'X':
            empty.append((i, j))
        elif M[i][j] == 'T':
            teachers.append((i, j))

for walls in combinations(empty, 3):
    for wall in walls:
        x, y = wall
        M[x][y] = 'B'
    if findS():
        print('YES')
        break
    for wall in walls:
        x, y = wall
        M[x][y] = 'X'
else:
    print('NO')