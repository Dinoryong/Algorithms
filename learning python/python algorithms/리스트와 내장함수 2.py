"""
len(list)
- list에 값이 몇 개 있는가

enumerate(list)
- tuple 형태로 (index number, value)

for index, value in enumerate(a):
    print(index, value)
- index number와 value 같이 출력

"""
a=[23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x)
print()

for x in a:
    if x%2 == 1:
        print(x, end=' ')
print()

for x in enumerate(a):
    print(x)
print()


''' 
tuple
- 값을 변형시킬 수 없다
'''
b = (1, 2, 3, 4, 5)
print(b[0])
# TypeError: 'tuple' object does not support item assignment
# b[0]=7

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()


""" 
if all(조건문 for x in list):


"""
if all(60>x for x in a):
    print("YES")
else:
    print("NO")

if any(11>x for x in a):
    print("YES")
else:
    print("NO")






