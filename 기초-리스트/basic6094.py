# 이상한 출석 번호 부르기3
# 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

n = int(input())
k = input().split()

for i in range(n):
    k[i] = int(k[i])

min = k[0]
for i in range(n):
    if(k[i] < min):
        min = k[i]

print(min)
