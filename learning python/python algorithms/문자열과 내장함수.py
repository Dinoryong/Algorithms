"""
문자열과 내장함수

string.upper()
- 다 대문자로 바꿔준다. 원본은 그대로

string.lower()
- 다 소문자로 바꿔준다. 원본은 그대로

string.find('T')
- 찾고자 하는 알파벳의 가장 처음 인덱스값을 돌려준다

string.count('T')
- 찾고자 하는 알파벳이 몇 개인지.

string[start:end:steps]




"""
msg="It is Time"
print(msg.upper())
print(msg.lower())
print(msg)

tmp=msg.upper()
print(tmp)
print(tmp.find('T'))
print(tmp.count('T'))
print(msg[:2])
print(msg[3:5])

"""
len(string)
- 문자열의 길이

for i in range(len(string)):
    print(string[i], end=' ')
- 문자열 하나씩 접근

string.isupper()
- 문자열이 대문자이면 참

string.islower()
- 문자열이 소문자이면 참

string.isalpha()
- 문자열이 알파벳일때만 참
- 문자열에서 공백을 제거하기 위해 쓴다
"""

print(len(msg))
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.isupper():
        print(x, end='')
print()

for x in msg:
    if x.islower():
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha():
        print(x, end=' ')
print()



'''
아스키코드
- A:65 ~ Z:90
- a:97 ~ z:122

ord(string)
- 아스키 코드를 차례대로 출력

chr(string)
- 아스키 코드에 대응하는 알파벳 출력
'''
tmp='AZ'
for x in tmp:
    print(ord(x))

tmp='az'
for x in tmp:
    print(ord(x))

tmp=65
print(chr(tmp))









