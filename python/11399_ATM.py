## 누적합 개념을 적용한 표준 코드
# import sys

# input = sys.stdin.readline;

# person = int(input());
# waitLine = list(map(int, input().split()));

# waitCount = 0;
# totalCount = 0;

# # 빠른 사람 대로 줄 다시 서기
# waitLine.sort();

# for i in range(person):
#     # 대기 시간에 자기가 걸린 시간 추가
#     waitCount += waitLine[i];
#     # 대기 시간 추가
#     totalCount += waitCount;

# sys.stdout.write(str(totalCount));

### 내가 푼 코드 

import sys

input = sys.stdin.readline;

person = int(input());
waitLine = list(map(int, input().split()));

waitCount = 0;
totalCount = 0;

# 빠른 사람 대로 줄 다시 서기
waitLine.sort();

for i in range(person):
    # 처음 사람
    if i == 0:
        # 자기가 걸린 시간만
        totalCount += waitLine[i];
        # 대기 시간 추가
        waitCount += waitLine[i];
    # 처음 사람과 중간 사람을 제외한 나머지 사람 
    elif i != (person-1) and i != 0:
        # 인출시간만큼 대기시간 추가
        waitCount += waitLine[i];
        # 인출 시간을 총 시간에 추가
        totalCount += waitCount;
    # 마지막 사람
    else:
        # 지금까지 걸린 대기시간
        totalCount += waitCount;
        # 마지막 사람 인출 시간 
        totalCount += waitLine[i];

sys.stdout.write(str(totalCount));

'''
atm 1대 -> n명의 사람들
 - i 번 사람(1000) -> p분 걸림(1000) -> 최소 시간
 - 이중 포문 가능? 
'''