# 16 : 45
import sys

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

n, c = map(int, user_input().split());
loc = [int(user_input()) for _ in range(n)];
loc.sort();

# 가장 긴 거리는 맨 처음과 맨 끝과의 거리 차
start, end = 1, max(loc) - loc[0];
answer = 0;

while start <= end:
    cnt = 1;
    # 현재 위치 지정 
    cur = loc[0];    
    mid = (start + end) // 2;

    for idx in range(1, len(loc)):
        #  임의의 거리와 현재 거리를 더했을 때보다 클 경우
        if loc[idx] >= cur + mid:
            # 공유기 설치하고 현재 위치 갱신
            cnt += 1;
            cur = loc[idx];
    # 공유기가 더 많이 설치된 경우 -> 거리 늘림
    if cnt >= c:
        start = mid + 1;
        answer = mid;
    else:
        end = mid - 1;

user_print(str(answer));
'''
최대한 많은 곳에서 와이파이를 사용해야 함
한 집에 공유기 하나만을 설치
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치
-> 거리를 통한 이진 탐색
'''