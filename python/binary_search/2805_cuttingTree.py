# 15:40
import sys

user_input = sys.stdin.readline;
user_print = sys.stdout.write;
# 나무의 수, 상근이가 가져가려는 나무의 길이
n, m = map(int, user_input().split());

treeHeights = (list(map(int, user_input().split())));

def cuttingTree(arr, start, end, h):
    while start <= end:
        # 자른 나무의 길이
        total = 0;
        mid = (start + end) // 2;

        for i in arr:
            if i >= mid:
                total += i - mid; 
        # 나무의 길이를 기준으로 탐색을 해야 함
        if total >= h:
            start = mid + 1;
        elif total < h:
            end = mid - 1
    return end;

end = max(treeHeights);
user_print(str(cuttingTree(treeHeights, 1, end, m)));

'''
- h 높이만큼 나무를 자름 (h보다 낮은 높이의 나무는 잘리지 않음)
- 집으로 가져가려는 나무의 길이 : m
- 나무의 높이가 n개 만큼 리스트로 주어짐
- n max 백만 개 -> O(n), O(logn)
- 나무를 최대한 덜 잘라야 함

4 7
20 15 10 17
10 15 17 20
10 부터 20까지 탐색
m개의 나무를 잘랐으면 break
'''
