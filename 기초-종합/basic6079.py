# 언제까지 더해야 할까?
# 1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가,
# 입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력한다.

a = int(input())
sum = 0
i = 1

while(1):
    sum += i

    if (sum >= a):
        print(i)
        break
    else:
        i += 1

