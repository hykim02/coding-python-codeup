# 바둑알 십자 뒤집기

a = []

 # 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력
for i in range(19):
    a.append([])
    b = input().split()

    for j in range(19):
        b[j] = int(b[j])
    
    a[i].append(b)

for x in range(19):
    for y in range(19):
        print(a[x][y], end = ' ')
    print()

# 십자 뒤집기 횟수(n)가 입력
num = int(input())

# 십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수
for i in range(num):
    x, y = map(int, input().split())

    # 가로줄 십자 뒤집기
    for h in a[x]:
        if(a[x] == 1):
            a[x] = 0
        else:
            a[x] = 1

    # 세로줄 십자 뒤집기
    for v in range(19):
        if(a[v][y] == 1):
            a[v][y] = 0
        else:
            a[v][y] = 1

# 바둑판 출력
for x in range(1, 19):
    for y in range(1, 19):
        print(a[x][y], end = ' ')