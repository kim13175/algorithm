import sys

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

glass = int(user_input());
lst = [0 for _ in range(10000)];
for i in range(glass):
    lst[i] = int(user_input());

table = [0 for _ in range(10000)];

# 첫 잔과 둘 째잔은 무조건 마시게 됨
table[0] = lst[0];
table[1] = lst[0] + lst[1];
table[2] = max(table[1], lst[0] + lst[2], lst[1] + lst[2])
# 3가지 경우
for i in range(3, glass):
    fstCase = table[i-1];
    sndCase = table[i-2] + lst[i];
    trdCase = table[i-3] + lst[i-1] + lst[i]
    table[i] = max(fstCase, sndCase, trdCase);

user_print(str(table[glass-1]));
'''
910
7 910
67 910   
'''