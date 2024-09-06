import sys

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

n = int(user_input());
numArr = list(map(int, input().split()));
# 감소하는 부분 수열 길이 담은 배열
countArr = [1 for _ in range(n)];

for i in range(1, n):
    for j in range(i):
        # 다음 인덱스 숫자가 클 경우 -> 증가가 일어남
        if numArr[i] > numArr[j]:
            # 현재 카운트 배열 요소, 이전 카운트 배열 요소에 + 1을 한 값
            countArr[i] = max(countArr[i], countArr[j] + 1);

user_print(str(max(countArr)));

