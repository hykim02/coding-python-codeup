# 점수 입력받아 평가 출력하기
# 점수 범위 : 평가
# 90 ~ 100 : A
# 70 ~  89 : B
# 40 ~  69 : C
#  0 ~  39 : D

a = input()
a = int(a)

if (a >= 90 and a <= 100):
    print("A")
elif (a >= 70 and a <= 89):
    print("B")
elif (a >= 40 and a <= 69):
    print("C")
else:
    print("D")