# 그림 파일 저장용량 계산하기

w, b, h = map(int, input().split())
result = w*b*h/8/1024/1024
print("%.2f"%result, "MB")