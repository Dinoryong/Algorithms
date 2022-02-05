'''
항상 main script 위에 함수를 만들어야 컴퓨터가 인식한다


'''
def add(a, b):
    c = a + b
    print(c)

add(3, 2)


def add(a, b):
    c = a+b
    # 함수의 값을 return 하고 !! 종료된다 !!
    return c

# x = add(3,2)
# print(x)
print(add(3, 2))


def add(a, b):
    c=a+b
    d=a-b
    # 여러 값이 있따면 tuple로 return 된다
    return c, d
print(add(3,2))


"""

"""
def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True


a = [12, 13, 7, 9, 19]
for y in a:
    # 참일 때 y 출력
    if isPrime(y):
        print(y, end=' ')










