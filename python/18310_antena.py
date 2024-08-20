'''
# 그리디 가능할까..?

import sys

input = sys.stdin.readline;

house = int(input());
locArr = list(map(int, input().split()));

startPoint = 0;
endPoint = len(locArr);
distance = 99999;
pickHouse = 0;

# 오름차순 정렬
locArr.sort();

for loc in locArr:
    # 각 집마다의 시작 지점
    startPoint = loc;
    per_distance = 0;
    for i in range(endPoint):
        # 임의 지점과 다른 지점들의 합
        if(loc != locArr[i]):
            per_distance += abs(loc - locArr[i]);
        # 같은 지점일 경우 거리는 없음
        else:
            per_distance += 0;
    # 더 짧은 경로가 나올 경우 기록 후 갱신
    if distance > per_distance:
        distance = per_distance;
        pickHouse = startPoint;
    # 경로의 비용이 같을 경우에는 적은 번호의 집으로 바꿈
    elif (distance == per_distance and pickHouse > startPoint):
        pickHouse = startPoint;

# 정답 출력
sys.stdout.write(str(pickHouse));

'''

# 그냥 중앙 값으로 하면 됨 ㅠㅠ
import sys
input = sys.stdin.readline

house = int(input());
locArr = list(map(int, input().split()));
pickHouse = 0;

# 내림 차순 정렬
locArr.sort();

# 배열은 0부터 인덱스 카운팅
if house % 2 == 0:
    pickHouse = locArr[(house // 2) - 1];
else:
    pickHouse = locArr[(house // 2)];    

sys.stdout.write(str(pickHouse));

'''
집의 개수와 위치한 거리 
총 거리는 마지막 집이 위치한 거리 -> 오름차순 정렬
집이 있는 위치에 부터 시작
    절대 값으로 음, 양의 부호 배제시킴
가장 짧은 총 거리로 설치할 수 있는 집 여러개일 경우 가장 작은 값 
'''