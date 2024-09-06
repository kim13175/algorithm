import sys
from collections import deque

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

n, m = map(int, user_input().split());
mapArr = [list(map(int, user_input().strip())) for _ in range(n)];

def bfs(arr):
    q = deque();
    q.append((0, 0));

    # 상 하 좌 우
    dx = [0, 0, -1, 1];
    dy = [-1, 1, 0, 0];

    while q:
        x, y = q.popleft();
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue;
            if arr[nx][ny] == 0:
                continue;
            # 갈 수 있는 길일 경우
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1;
                q.append((nx, ny));
    return arr[n-1][m-1];

user_print(str(bfs(mapArr)));
