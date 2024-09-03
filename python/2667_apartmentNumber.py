import sys
from collections import deque

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

n = int(user_input());
# 입력된 문자열 각 요소로 받을 땐 strip() 사용
map = [list(map(int, user_input().strip())) for _ in range(n)];

dx = [1, 0, -1, 0];
dy = [0, 1, 0, -1];

def bfs(arr, a, b):
    q = deque();
    q.append((a, b));
    arr[a][b] = 0;
    cnt = 1;

    while q:
        x, y = q.popleft();
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            # 범위 초과
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue;
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0;
                q.append((nx, ny));
                cnt += 1;
    return cnt

cnt = [];
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            cnt.append(bfs(map, i, j));

cnt.sort();
user_print(str(len(cnt)) + '\n');
for i in range(len(cnt)):
    user_print(str(cnt[i]) + '\n');