# 정수 1개 입력받아 그 수까지 출력하기2
# range(끝)
# range(시작, 끝)
# range(시작, 끝, 증감)
# 시작 수는 포함이고, 끝 수는 포함되지 않는다. [시작, 끝)

a = input()
a = int(a)

for i in range(a+1):
    print(i)