# 3 6 9 게임의 왕이 되자

num = int(input())

for i in range(1, num+1):
    rest = i % 10 # 나머지
    if (rest == 0):
        print(i, end = ' ')
    elif (rest % 3 == 0):
        print("X", end = ' ')
    else:
        print(i, end = ' ')