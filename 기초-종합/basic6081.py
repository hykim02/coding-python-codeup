# 16진수 구구단 출력하기

a = int(input(), 16)

for i in range(1, 16):
    print("%X*%X=%X" % (a, i, a*i))
    # print("%X"%a, "*%X"%i, "=%X"%(a*i), sep = '')
    