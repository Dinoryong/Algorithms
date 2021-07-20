# prg_H-Index

----

[프로그래머스 H-Index](https://programmers.co.kr/learn/courses/30/lessons/42747)

<br/>

## Topics

- Array

<br/>

## Sketch

- range 안에 max() 를 주면 범위가 정렬 된다

- citations을 정렬 혹은 역정렬한다

- 해당 논문에서 인용된 횟수 >= 전체에서 인용된 논문의 수    

  일 때 , h의 값이 최대가 된다.

<br/>

## Wrong Answer

- 주의해야 할 케이스가 뭐가 있을까....
- 주의해야 할 python 문법, range 뭐가 있을까...

```python
```



<br/>

## Solved

- fs

```python
# sol 1. 정렬
# 정확성: 100.0 / 합계: 100.0 / 100.0
def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i
    return 0

# sol 2. range 에서 max() 써서
def solution(citations):
    for i in range(max(citations), -1, -1):
        if sum(1 for j in citations if j >= i) >= i:
            break
    return i

# sol 3. 역정렬
def solution(citations):
    citations.sort(reverse=True)
    for i, n in enumerate(citations):
        if n <= i:
            return i
    return len(citations)
```



