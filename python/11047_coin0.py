import sys 

input = sys.stdin.readline
n, k = map(int, input().split());

coinCnt = 0;

coinValue = [];

for i in range(n):
    a = int(input());
    coinValue.append(a);

# 가치가 큰 순부터 내림차순
coinValue.reverse();

for coin in coinValue:
    # 만들 가치보다 작으면서 제일큰 동전
    if k >= coin:
        # 최대한 많이 뽑아냄
        cnt = k // coin;
        # 남은 돈 = 가치 
        k = k % coin;
        coinCnt += cnt;

sys.stdout.write(str(coinCnt));

'''
n개의 코인 종류 적절히 사용해서 총 k의 가치를 만드는 동전 개수 최소 값
 -> 최소 동전 개수라면 가치가 제일 큰 동전부터 비교해야 함
'''