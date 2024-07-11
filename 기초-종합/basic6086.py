# 거기까지! 이제 그만~

num = int(input())
a = 0
b = 0

while(True):
    a += 1 # 더할 숫자
    b += a 
    
    if(b >= num):
        break

print(b)
