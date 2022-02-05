"""
중첩 반복문

"""
# 점점 커지는 별 찍기
for i in range(5):
    for j in range(i+1):
        print("*", end=' ')
    print() # 줄바꿈

# 점점 작아지는 별 찍기
for i in range(5):
    for j in range(5-i):
        print("*", end=' ')