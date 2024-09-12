import sys

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

n = int(user_input());
lst = [list(map(int, user_input().split())) for _ in range(n)];

cntArr = [0] * 3;

def partialSearch(x, y, n):
    paper = lst[y][x];

    for r in range(y, y+n):
        for c in range(x, x+n):
            if lst[r][c] != paper:              
                # 9개로 자름
                splitN = n // 3;
                # 9개로 나눈면 들을 재귀문을 통해 탐색
                for i in range(3):
                    for j in range(3):
                        partialSearch(x + (splitN * i), y + (splitN * j), splitN);
                
                return
    # 같을 경우 종이 추가 (배열은 0부터)
    cntArr[paper + 1] += 1;
    return;
        

partialSearch(0, 0, n);
for idx in range(3):
    user_print(str(cntArr[idx]));
    user_print('\n');

'''
종이가 모두 같은 수일 경우 종이 그대로 사용
다를 경우 같은 크기의 종이 9개로 자르고 다시 확인
-1, 0, 1로 채워진 종이의 개수를 줄마다 출력

9 개로 나눔 
-> 0 : 3, 1 : 2, -1 : 1 - 한번 9개로 자름
-> 0 : 9, 1 : 9, -1 : 9
10 12 11
'''