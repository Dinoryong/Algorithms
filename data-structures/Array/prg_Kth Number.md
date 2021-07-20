# K번째 수

-----

[프로그래머스 K번째 수](https://programmers.co.kr/learn/courses/30/lessons/42748)



## Topics

- Array



## Sketch

- index에 주의
- array indexing 활용하여 i, j, k 값 추출하고
- 오름차순으로 배열을 다시 정렬한 후에
- 새로운 배열의 k번째 수를 indexing 으로 구한다. 



## Wrong Answer

- 변수에 command[x] 를 할당해줘야한다
- sort 할 때는 array.sort() 를 바로 해주면 된다.

```python
def solution(array, commands):
    answer = []
    for command in commands:
        command[0] = i
        command[1] = j
        command[2] = k
        arr = array[i-1:j]
        arr = arr.sort()
        answer.append(arr[k-1])
    return answer
```



## Solved

```python
def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    return answer
```

