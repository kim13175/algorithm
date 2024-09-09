import sys

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

n, r, c = map(int, user_input().split());
N = 2 ** n;

cnt = 0;

def zSearch(x, y, n):
    global cnt;
    # 2 by 2 : 4분면 분할
    if n == 2:
        if((x, y) == (0, 1)):
            cnt += 1;
        elif((x, y) == (1, 0)):
            cnt += 2;
        elif((x, y) == (1, 1)):
            cnt += 3;
        return;
    # 전체 1사분면
    if (x < n // 2 and y >= n // 2):
        cnt += n * n // 4;
        zSearch(x, y - n // 2, n // 2);
    # 전체 3사분면
    elif (x >= n // 2 and y < n // 2):
        cnt += n * n // 2;
        zSearch(x - n // 2, y, n // 2);
    # 전체 4사분면
    elif (x >= n // 2 and y >= n // 2):
        cnt += 3 * n * n // 4;
        zSearch(x - n // 2, y - n // 2, n // 2);
    else:
        zSearch(x, y, n // 2);

zSearch(r, c, N);

user_print(str(cnt));
'''
0  1  4  5
2  3  6  7
8  9  12 13
10 11 14 15
'''