# 3 6 9 게임의 왕이 되자

num = int(input())

for i in range(1, num+1):
    if (i % 10 == 3):
        print("X", end = '')
    else:
        print(i)