# 수 나열하기2

a, r, n = map(int, input().split())

for i in range(n-1):
    a *= r

print(a)