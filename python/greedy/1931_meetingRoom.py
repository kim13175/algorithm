import sys

input = sys.stdin.readline;

taskArr = [];

meet = int(input());

for i in range(meet):
    start, end = list(map(int, input().split()));
    taskArr.append([start, end]);

# 종료 시간을 기준으로 내림차순 정렬
taskArr.sort(key=lambda x: (x[1], x[0]));
# 종료시간 비교하기 위한 변수
endTime = 0;
# 최대 회의 개수
task = 0;

for newStart, newEnd in taskArr:
    if endTime <= newStart:
        task += 1;
        endTime = newEnd;

sys.stdout.write(str(task));

'''
1. 회의 정보 - 시작 시간, 종료 시간
2. 한 방에 최대 잡을 수 있는 회의 개수
 - 종료시간이 작아야 한다 -> 다음 회의를 할 수 있는 경우의 수가 많아짐
'''
