# 정수 3개 입력받아 가장 작은 값 출력하기
# "순서에 따라 한 단계씩 실행"
# "미리 정해진 순서에 따라 하나씩 연산 수행"
# "그 때까지 연산된 결과를 이용해 다시 순서에 따라 하나씩 연산"

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
min =  (a if (a < b) else b) if ((a if (a < b) else b) < c) else c
print(min)