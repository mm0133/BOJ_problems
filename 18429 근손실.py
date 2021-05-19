N, K = map(int, input().split())
A = list(map(int, input().split()))
vis = [0] * N
answer = 0

def backtrack(w, t):
    if t == N:
        global answer
        answer += 1
        return
    for i in range(N):
        if vis[i] == 0 and w + A[i] - K >= 0:
            vis[i] = 1
            backtrack(w + A[i] - K, t + 1)
            vis[i] = 0
backtrack(0, 0)
print(answer)
