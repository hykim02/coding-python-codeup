# 그림 파일 저장용량 계산하기

w, b, h = map(int, input().split())
result = w*b*h/8/1024/1024
print("%.2f"%result, "MB") # round 사용하면 불필요한 0은 없애버리기 때문에 오답처리