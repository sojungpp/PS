from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
N, M = map(int, input().split())
board = [input() for _ in range(N)]


def is_valid(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    dq = deque()
    # d = 칸 수
    dq.append((0, 0, 1))
    while dq:
        y, x, d = dq.popleft()

        # 목적지에 도착한 경우
        if y == N - 1 and x == M - 1:
            return d

        nd = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, nd))


print(bfs())
