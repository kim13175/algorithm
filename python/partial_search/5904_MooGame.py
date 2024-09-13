import sys

user_input = sys.stdin.readline;
user_print = sys.stdout.write;

n = int(user_input());
# s(0) = 'moo'
k = 1;
length = 3;

def Moo(k, leng, n):
    # s(k) == s(0) : 'moo'
    if n <= 3:
        if n == 1:
            return "m";
        else:
            return "o";
    # s(1) = s(0) / { mid : m + {o * (1+2)} } / s(0)
    mid = k + 3;
    left = (leng - mid) // 2;
    # 왼족
    if n <= left:
        return Moo(k-1, left, n);
    # 오른쪽
    elif n > (left + mid):
        return Moo(k-1, left, n - (left + mid));
    else:
        # 시작부분은 무조건 m이 옴
        if left + 1 == n:
            return "m";
        else:
            return "o";

# n의 크기가 문자열의 길이보다 작아질 때 까지 
while True:
    # s(1) = s(0) / m {o * (1+2)} / s(0)
    length = 2 * length + 3 + k;
    if length > n:
        break;
    k += 1;

user_print(str(Moo(k, length, n)));



'''
s(k) = s(k-1) + o * (k+2) + s(k-1)
s(0) = m o o /
s(1) = s(0) / m {o * (1+2)} / s(0)
s(2) = s(1) / m {o * (2+2)} / s(1) 
'''