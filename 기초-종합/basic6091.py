# 함께 문제 푸는 날
# 같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는,
# 방문 주기가 공백을 두고 입력된다. (단, 입력값은 100이하의 자연수이다.)

a, b, c = map(int, input().split())
day = 1

while((day % a != 0) or (day % b != 0) or (day % c != 0)):
    day += 1

print(day)