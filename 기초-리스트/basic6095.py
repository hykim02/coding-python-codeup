# 바둑판에 흰 돌 놓기


# 19x19 바둑판 생성
d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

# 흰 바둑 놓기
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    d[x][y] = 1


for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end = ' ')
    print()
