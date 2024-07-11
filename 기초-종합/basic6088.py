# 수 나열하기1
# 시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)

a, d, n = map(int, input().split())

for i in range(n-1):
    a += d

print(a)