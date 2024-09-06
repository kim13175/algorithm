import sys
from collections import deque

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

x, y = map(int, input().split());
q = deque();

maxLen = 100005;
cntArr = [0] * maxLen;

def bfs(start, end):
    q.append(start);
    while q:
        x = q.popleft();
        if x == end:
            return cntArr[x];
            # 동생을 찾았을 경우 중단
            break;
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < maxLen and cntArr[nx] == 0:
                cntArr[nx] = cntArr[x] + 1;
                q.append(nx);

user_print(str(bfs(x, y)));
'''
0 ~ 100000 사이의 점에 위치
- 걸을 경우 1초에 한칸 순간이동 1초에 0부터 현재까지 거리 만큼 이동 가능
- 수빈이가 동생의 거리만큼 가서 찾는 최단 시간
    걸을 경우(+1 / -1) / 순간 이동 할 경우
'''