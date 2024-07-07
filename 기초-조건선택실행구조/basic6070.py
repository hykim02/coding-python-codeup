# 월 입력받아 계절 출력하기
# 12, 1, 2 : winter
# 3, 4, 5 : spring
# 6, 7, 8 : summer
# 9, 10, 11 : fall

a = input()
a = int(a)

if ((a // 3) == 1):
    print("spring")
elif ((a // 3) == 2):
    print("summer")
elif ((a // 3) == 3):
    print("fall")
else:
    print("winter")