'''
a=[]
- 빈 리스트 만들기

b=list()
- 빈 리스트 만들기

list.append(문자,숫자)
- 리스트 맨 뒤에 값 추가

list.insert(index 번호, 추가할 값)
- 리스트의 정확한 index number 지점에 특정 값 추가하기

list.pop()
- 리스트의 맨 뒤에 있는 값을 리스트에서 제거한다

list.pop(index 번호)
- 리스트의 정확한 index number 값을 리스트에서 제거한다

list.remove(값)
- 리스트에서 특정 값을 찾아서 제거한다.
'''
import random as r
a=[]
# print(a)
b=list()
# print(b)

a=[1,2,3,4,5]
# print(a)
# print(a[0])

b=list(range(1, 11))
# print(b)

c=a+b
# print(c)

print(a)
a.append(6)
print(a)

a.insert(3, 7)
print(a)

a.pop()
print(a)
a.pop(3)
print(a)
a.remove(4)
print(a)


"""
list.index(값)
- 리스트에서 특정 값을 찾고 그 index number 반환
"""


print(a.index(5))


"""
sum(list)
- 리스트 안의 모든 값을 더한 결과값

max(list)
- max 라는 함수의 인자로 list 가 넘어가면, 리스트 내부 값들 중에서 
제일 큰 값을 찾아준다

min(list)
- min 이라는 함수의 인자로 list 가 넘어가면 , 리스트 내부 값들 중에서
제일 작은 값을 찾아준다.

max(인자 값, 인자값, 인자값)
- 인자값들 중에서 제일 큰 값을 찾아준다

import random as r
r.shuffle(list)
- 정렬을 섞어준다

list.sort()
- 오름차순 정렬

list.sort(reverse=True)
- 내림차순 정렬

list.clear()
- 리스트 요소를 다 지우고 빈 리스트로 만든다
"""
a = list(range(1, 11))
print(a)

print(sum(a))
print(max(a))
print(min(a))
print(min(7, 5))

print(a)
r.shuffle(a)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.clear()
print(a)




"""

"""




