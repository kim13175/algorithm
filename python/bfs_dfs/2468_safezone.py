import sys
from collections import deque

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

n = int(user_input());
zone = [list(map(int, user_input().split())) for _ in range(n)];

maxNum = 0;
for i in range(n):
    maxNum = max(zone[i]);

# 하 상 좌 우
dx = [0, 0, -1, 1];
dy = [-1, 1, 0, 0];
q = deque();

def bfs(a, b, h):
    q.append((a, b));
    visited[a][b] = 1;

    while q:
        x, y = q.popleft();

        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue;
            # 방문하지 않았던 안전구역일 경우 방문 처리 
            if zone[nx][ny] > h and visited[nx][ny] == 0:
                visited[nx][ny] = 1;
                # 새로운 위치 추가
                q.append((nx, ny));

answer = 0;
for k in range(maxNum):
    # 매 높이마다 새로운 배열 생성
    visited = [[0] * n for _ in range(n)];
    cnt = 0;

    for i in range(n):
        for j in range(n):
            if zone[i][j] > k and visited[i][j] == 0:
                bfs(i, j, k);
                cnt += 1;
    
    # 매 높이마다 최대값 비교
    answer = max(answer, cnt);

user_print(str(answer));