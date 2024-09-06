import sys

n, m, b = map(int, sys.stdin.readline().split());
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)];
fl = 257;
result = sys.maxsize;

# 각 좌표의 땅의 높이까지 반복 (땅의 최대 높이까지 반복해봐야 알 수 있음)
for floor in range(fl):
    extractionBlock, putBlock = 0, 0; 
    for row in range(n):
        for col in range(m):
            if ground[row][col] > floor:
                extractionBlock += ground[row][col] - floor;
            else:
                putBlock += floor - ground[row][col];

    if extractionBlock + b >= putBlock :
        # 블록 추출 2초, 블록 넣기 1초 합한 결과가 result보다 작으면
        if (extractionBlock * 2) + putBlock <= result:
            result = (extractionBlock * 2) + putBlock;
            # 땅의 높이 확인
            height = floor;

print(result, height);

'''
1. 1번 작업 좌표의 가장 위에 있는 블록을 제거하여 인벤토리에 넣음 -> 1초 걸림
2. 2번 작업 인벤토리에서 블록 하나를 꺼내어 좌표의 가장 위에 있는 블록 위에 놓는다 -> 2초 걸림
3. 최소시간과 땅의 높이 출력

solution
- 블록 빼기 2초 다른 블록이 적을 경우
- 블록 넣기 1초 다른 블록이 많을 경우
- 전부 비교해서 같은 값이 적은 쪽을 기준, 추출한 블록과 넣을 블록을 분리
'''