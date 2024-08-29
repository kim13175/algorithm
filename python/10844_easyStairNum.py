
import sys

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

n = int(input());
table = [[0]*10 for _ in range(n+1)];

answer = 0;
for i in range(1, 10):
    table[1][i] = 1;

mod = 1000000000;

for i in range(2, n+1):
    for j in range(10):
        # 앞에 있는 수가 0일 때
        if j == 0:
            table[i][j] = table[i-1][1];
        # 앞에 있는 수가 9일때
        elif j == 9:
            table[i][j] = table[i-1][8];
        else:
            table[i][j] = table[i-1][j-1] + table[i-1][j+1];

print(sum(table[n]) % mod);

'''
길이가 n인 계단 수
'''