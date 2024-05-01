# 참/거짓이 서로 다를 때에만 참 출력하기
# 참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을 XOR(exclusive or, 배타적 논리합) 연산이라고도 부른다.

a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and not(b)) or (not(a) and b))
print(a ^ b)