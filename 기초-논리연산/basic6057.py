# 참/거짓이 서로 같을 때에만 참 출력하기
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and b) or ((not a) and (not b)))
