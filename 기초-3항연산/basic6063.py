# 정수 2개 입력받아 큰 값 출력하기
# 3개의 요소로 이루어지는 3항 연산은 "x if C else y" 의 형태로 작성이 된다.
a, b = input().split()
a = int(a)
b = int(b)
c = (a if(a >= b) else b)
print(c)