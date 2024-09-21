# 16 : 40
import sys

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

k, n = map(int, user_input().split());

length = [int(user_input()) for _ in range(k)];

start, end = 1, max(length);

while start <= end:
    mid = (start + end) // 2;
    total = 0;
    # 각 선마다 임의의 길이만큼 나누고 더함
    for leng in length:
        total += leng // mid;
    # 요구 개수보다 많을 경우
    if total >= n:
        start = mid + 1;
    else:
        end = mid - 1;

# 최대 선의 길이는 탐색 중 가장 뒤에 있는 수가 됨 
user_print(str(end));

'''
각 선마다의 선을 잘라 총 n개의 랜선을 만들어야 함

802 - 200 4
743 - 200 3
457 - 200 2
539 - 200 2
'''