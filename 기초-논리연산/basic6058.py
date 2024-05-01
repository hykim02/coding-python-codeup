# 둘 다 거짓일 경우만 참 출력하기
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a == False) and (b == False))
print(not a and not b)
print(not a)