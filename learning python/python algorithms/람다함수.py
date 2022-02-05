'''
내장함수의 인자로 쓰기 좋다
익명함수
sort 같은 경우

'''
def plus_one(x):
    return x+1

print(plus_one(1))


'''
map(함수명, 자료)
- 자료들을 함수화시켜라

'''
plus_two = lambda x: x+2
print(plus_two(1))

###
a = [1, 2, 3]
print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a)))











