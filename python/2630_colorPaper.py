import sys
from collections import deque

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

n = int(user_input());
table = [list(map(int, user_input().split())) for _ in range(n)];

paper = [0, 0];

def partial(x, y, n):

    color = table[x][y];
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 색종이이 색이 다를 경우
            if color != table[i][j]:
                # 4분할로 탐색
                partial(x, y, n // 2);
                partial(x, y + n // 2, n // 2);
                partial(x + n // 2, y, n // 2);
                partial(x + n // 2, y + n // 2, n // 2);
                return;
    if color == 0:
        paper[0] += 1;
    else :
        paper[1] += 1;

partial(0, 0, n);
user_print(str(paper[0]) + '\n' + str(paper[1]));

'''
하얀색과 파란색 색종이는 1과 0으로 구분
잘라진 영역에는 한 색의 종이만 있어야 함
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1


'''