import sys

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

n = int(input());
continueSum = list(map(int, input().split()));
table = [continueSum[0]] + [0] * (n - 1); 

for i in range(1, n):
    table[i] = max(table[i-1] + continueSum[i], continueSum[i]);

user_print(str(max(table)));

'''
- 연속된 몇개의 수의 합 중 최대?
 -> 합을 계산할 때마다 max값을 체크  
'''