# Learning Python

-----

[toc]

<br/>

### enumerate 함수

- 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가집니다.
- enumerate는 “열거하다”라는 뜻입니다.
- 이 함수는 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴합니다.
- 보통 enumerate 함수는 for문과 함께 자주 사용됩니다.

<br/>

### dictionary

- {key : value}
- 

<br/>

### zip

- `zip(*iterable)`
- 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수

-  `*iterable`은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미

  ```python
  list(zip([1, 2, 3], [4, 5, 6]))
  >>> [(1, 4), (2, 5), (3, 6)]
  
  list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
  >>> [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
  
  list(zip("abc", "def"))
  >>> [('a', 'd'), ('b', 'e'), ('c', 'f')]
  ```

- references : [점프 투 파이썬](https://wikidocs.net/32#zip)

<br/>

### map

- 리스트의 요소를 지정된 함수로 처리해주는 함수
- 맵 객체 map object 생성 시, 안에 들어있는 값을 볼 수 없으므로 주로 list 사용해 list로 출력
- 원본 요소를 변경하지 않고 새 리스트를 생성
  - e.g) 리스트의 모든 요소를 int 를 사용해서 변환 -> list 사용해서 map의 결과를 다시 리스트로 만들어준다. 

```python
# 실수가 저장된 리스트가 있을 떄 , 이 리스트의 모든 요소를 정수로 변환
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)
>>> [1, 2, 3, 4]
```

- map 이 반환하는 맵 객체는 이터레이터라서 변수 여러 개에 저장하는 unpacking 가능
  - a, b = map(int, input().split())을 풀어서 쓰면 다음과 같은 코드가 된다

```python
x = input().split()    # input().split()의 결과는 문자열 리스트
m = map(int, x)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
a, b = m               # 맵 객체는 변수 여러 개에 저장할 수 있음
```

- ref : [코딩 도장](https://dojang.io/mod/page/view.php?id=2286)

<br/>

### lambda

- `lambda 인자 : 표현식`
- 한 줄 짜리 익명함수
- 활용 : `map()` , `reduce()` , `filter()`
- ref : [왕초보를 위한 Python](https://wikidocs.net/64)

<br/>

### reduce()

- `reduce(함수, 시퀀스)`
- 시퀀스의 원소들을 누적적으로 함수에 적용시킨다

```python
from functools import reduce   # 파이썬 3에서는 써주셔야 해요  
reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])

>> 10
```

```python
reduce(lambda x, y: y + x, 'abcde')

>>> 'edcba'
```

- ref : [왕초보를 위한 Python](https://wikidocs.net/64)

이해가 안 된다. 다시 !

<br/>

### filter()

- `filter(함수, 리스트)`
- 리스트에 들어있는 원소들을 함수에 적용시켜서 결과가 참인 값들로 새로운 리스트를 만들어준다

```python
# 0 부터 9까지의 리스트 중에서 5보다 작은 것만 돌려주는 예제
list(filter(lambda x: x < 5, range(10)))
>>> [0, 1, 2, 3, 4]

# 홀수를 돌려주는 예제
list(filter(lambda x: x % 2, range(10)))
>>> [1, 3, 5, 7, 9]
```

- ref : [왕초보를 위한 Python](https://wikidocs.net/64)

<br/>

### ASCII

- 
- 표 눈에 익히기

- 문자열 비교는 ASCII 값으로 치환되어 정렬해볼 수 있다.

<br/>

### String 대소 비교

- f

<br/>

### join

- `"".join(리스트)`

- `'구분자'.join(리스트)`

```python
# 원본 리스트
a = ['BlockDMask', 'python', 'example', 'happy new year']
print(a)
print()
 
# 리스트를 문자열로 합치기
result = ".\n".join(a)
 
print(result)

>>>BlockDMask.
python.
example.
happy new year
```

- references : [blog](https://blockdmask.tistory.com/468)

<br/>

### range에서 max()를 쓸 경우

- [프로그래머스 H-Index 풀이]()
- 

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>









