# 정수 1개 입력받아 분류하기
# 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D

a = input()
a = int(a)

# 음수
if (a < 0):
    if (a % 2 == 0):
        print("A")
    else:
        print("B")
# 양수
else:
    if (a % 2 == 0):
        print("C")
    else:
        print("D")