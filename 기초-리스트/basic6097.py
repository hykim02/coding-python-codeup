# 설탕과자 뽑기

# 격자판의 세로(h), 가로(w) 가 공백을 두고 입력
h, w = map(int, input("세로, 가로:").split())

# 격자판 생성
b = []

for i in range(h):
    b.append([])
    for j in range(w):
        b[i].append(0)
        

# 격자판 출력
for i in range(h):
    for j in range(w):
        print(b[i][j], end = " ")
    print()

# 놓을 수 있는 막대의 개수(n)
n = input("막대 개수:")
n = int(n)

# 각 막대의 길이(l), 방향(d: 가로는 0, 세로는 1), 좌표(x, y)가 입력
for i in range(n):
    l, d, x, y = map(int, input("길이, 방향, 좌표(x, y):").split())
    b[x-1][y-1] = 1 # 첫좌표 먼저 표시

    # 격자판 출력
    if(d == 0): # 가로인 경우
        y = y-1
        print("y:", y)
        for j in range(l-1): # 길이만큼 반복
            y += 1
            print("y:", y)
            b[x-1][y] = 1
    else: # 세로인 경우
        x = x-1
        print("x:", x)
        for j in range(l-1): # 길이만큼 반복
            x += 1
            print("x:", x)
            b[x][y-1] = 1

# 격자판 출력
for i in range(h):
    for j in range(w):
        print(b[i][j], end = " ")
    print()
