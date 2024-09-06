import sys

input = sys.stdin.readline;

# 문자열일 경우 input().rstrip() -> 개행문자 제거
sugar = int(input());

if sugar % 5 == 0:
    sys.stdout.write(str(sugar // 5));
else:
    bag = 0;
    # 설탕이 남아 있을 경우
    while sugar > 0:
        sugar -= 3; bag += 1;
        # 5kg 봉지에 담을 수 있는 경우
        if sugar % 5 == 0 and sugar > 0:

            bag += sugar // 5; 
            sys.stdout.write(str(bag)); break;
        # 3kg 봉지에 담아도 남는 경우
        elif sugar > 0 and sugar < 3:

            sys.stdout.write(str(-1)); break;
        # 설탕이 봉지에 다 담겨질 경우
        elif sugar == 0:

            sys.stdout.write(str(bag)); break;

'''
설탕 봉지 3kg, 5kg
더 적은 봉지의 개수를 들고 가려고 함
몇개의 봉지를 가져가야할지 구해라
-> 정확하게 못 담을 경우 -1
'''