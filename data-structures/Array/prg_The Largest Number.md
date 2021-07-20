# 가장 큰 수

-------------

[프로그래머스 가장 큰 수](https://programmers.co.kr/learn/courses/30/lessons/42746)



## Topics

- Array



## Sketch

- 값이 0일 때 case 주의
- numbers 의 원소는 0 이상 1,000 이하이기 때문에 3자리 수로 맞춰준 뒤에 비교한다
- 구한 numbers 값을 join 으로 문자열을 합쳐주고
- int 변환 후 다시 str 변환하여 , 모든 값이 0인 case를 처리해준다



## Wrong Answer

- return 할 때, 모든 값이 0일 떄 (즉, '000' 처리하기 위해) int로 변환한 뒤, 다시 str로 변환해야 한다

```python
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)

    return str(''.join(numbers))
```



## Solved

- 문자열 비교는 ASCII 값으로 치환한다는 것

```python
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)

    return str(int(''.join(numbers)))
```

- case 1 : n 의 원소가  0

numbers = [6, 10, 2, 0]

666 , 101010, 222, 000

numbers = [0, 0, 0, 0]

0

- case 2 : n 의 원소가 1000 

numbers = [6, 10, 2, 1000]

666, 101010, 222, 100010001000



