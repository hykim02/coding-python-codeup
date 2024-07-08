# 짝수 합 구하기

a = int(input())
sum = 0

for i in range(a+1):
    if (i % 2 == 0): # 짝수라면
        sum += i
    else:
        continue

print(sum)