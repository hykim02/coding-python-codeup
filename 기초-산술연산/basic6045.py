# 정수 3개 입력받아 합과 평균 출력하기
a, b, c = input().split()
sum = int(a) + int(b) + int(c)
avg = sum / 3
print(sum, format(avg, ".2f"))