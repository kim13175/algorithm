# 12:26
import sys
from collections import deque

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

n = int(user_input());
lst = [list(map(int, user_input().strip())) for _ in range(n)];

ans = '';

def quad(arr, x, y, n):
    global ans;
    flag = True;

    for r in range(x, x+n):
        if not flag:
            break;
        for c in range(y, y+n):
            if arr[x][y] != arr[r][c]:
                flag = False;
                break; 

    if not flag:
        splitN = n // 2;
        ans += "(";
        # 2사분면
        quad(arr, x, y, splitN);
        # 1사분면
        quad(arr, x, y+splitN, splitN);
        # 3사분면
        quad(arr, x+splitN, y, splitN);
        # 4사분면    
        quad(arr, x+splitN, y+splitN, splitN);
        ans += ")";
    else:
        ans += str(arr[x][y]);

quad(lst, 0, 0, n);
user_print(str(ans));
'''
00000000
00000000
00001111
00001111
00011111
00111111
00111111
00111111

(0
(0011)
(0
(0111)
01)
1)
4분면을 기준으로 계속 분할하되
전부 같은 수 일 경우 
그 수를 출력 
다른 수일 경우에는 또다시 4분면으로 분할
다 분할하여 2 by 2 행렬이 남았을 경우 그 배열 안의 수를 모두 출력
'''