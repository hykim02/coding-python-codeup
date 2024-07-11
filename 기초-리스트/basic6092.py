# 이상한 출석 번호 부르기1
# 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d = []  # 번호 리스트
for i in range(24):
    d.append(0)  # 값 0 대입

for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end = ' ')
