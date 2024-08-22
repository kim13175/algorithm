import sys

input = sys.stdin.readline().strip('\n');
print_ = sys.stdout.write;

subSplit = input.split("-");

numList = [];
sum = 0;
result = 0;

for part in subSplit:
    sum = 0; 
    addSplit = part.split('+');
    # + 부호 기준으로 양옆 숫자를 더해줌
    for num in addSplit:
        sum += int(num);
    numList.append(sum);

# 첫 시작 값은 더해야 함
result += numList[0];

for i in range(1, len(numList)):
    result -= numList[i];

print_(str(result));
    


'''
- 가장 처음과 마지막 문자는 숫자
- 부호가 나올 때의 부분을 나누면 될 듯
- + 가 나오면 앞과 전의 껄 더하면 됨 
- - 일 경우 더한 거를 뻬는 것이 제일 최소 값
    -> 괄호로 + 연산 먼저 진행
'''