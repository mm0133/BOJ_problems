import sys
from itertools import combinations

N = int(sys.stdin.readline())
M = []
for i in range(N):
    M.append(sys.stdin.readline().split())


# T 위치 -> 상하좌우 탐색 : s 만나면 멈추고 장애물 1 설치 만약 겹치는 부분이 존재한다면 장애물위치를 그걸로 옮기고원래 두개 하나로 갯수 합치기
# s위치 -> 상파좌우 탐색 : t만나면 멈추고 장애물 설치 

def findS():
    for teacher in teachers:
        x, y = teacher
        i = x
        j = y
        while 1:
            i -= 1
            if i < 0 or M[i][j] == 'B':
                break
            if M[i][j] == 'S':
                return False
        i = x
        j = y
        while 1:
            i += 1
            if i >= N or M[i][j] == 'B':
                break
            if M[i][j] == 'S':
                return False
        i = x
        j = y
        while 1:
            j -= 1
            if j < 0 or M[i][j] == 'B':
                break
            if M[i][j] == 'S':
                return False
        i = x
        j = y
        while 1:
            j += 1
            if j >= N or M[i][j] == 'B':
                break
            if M[i][j] == 'S':
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