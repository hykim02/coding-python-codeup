# 수 나열하기2
# 시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)

a, r, n = map(int, input().split())

for i in range(n-1):
    a *= r

print(a)