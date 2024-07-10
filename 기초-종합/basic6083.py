# 빛 섞어 색 만들기

r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
count = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k, sep = ' ') # 공백으로 연결
            count += 1

print(count)
