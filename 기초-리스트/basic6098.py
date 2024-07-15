# 성실한 개미 
# 10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력
miro = []

for i in range(10):
    a = input().split()

    for j in range(10):
        a[j] = int(a[j])
    miro.append(a)

# 개미 이동
# 오른쪽 or 아래쪽으로만 이동
# 먹이(2)를 찾거나 더 이상 이동할 수 없는 경우(1) stop
# 0인 길만 이동
# (2,2)에서 출발
# 지나간 길은 9로 표시
# 개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
# (오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

x = 1
y = 1
miro[x][y] = 9 # 첫 좌표
while(True):
    # 오른쪽 확인
    if(miro[x][y+1] == 0):
        y += 1 # 현재 위치 저장
        miro[x][y] = 9 # 이동
    elif(miro[x][y+1] == 2): # 먹이 발견 시
        y += 1 
        miro[x][y] = 9
        break
    else:
        # 아래쪽 확인
        if(miro[x+1][y] == 0):
            x += 1 # 현재 위치 저장
            miro[x][y] = 9 # 이동
        elif(miro[x+1][y] == 2): # 먹이 발견 시
            x += 1 
            miro[x][y] = 9
            break
        else:
            miro[x][y] = 9
            break

# 미로 출력
for i in range(10):

    for j in range(10):
        print(miro[i][j], end = " ")
    print()