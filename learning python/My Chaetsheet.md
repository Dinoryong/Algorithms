# My Cheatsheet

-----

> [toc]

## sort() vs sorted()

> [ref link](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wideeyed&logNo=221745416992)

### `<list>.sort()`

- 리스트형 메소드 => 리스트 원본값을 직접 수정
- *함수의 리턴값이 None* 이다. 정렬된 값은 리턴되지 않는다

``` python
a1 = [6, 3, 9]
print('a1 :', a1)   # a1 : [6, 3, 9]
a2 = a1.sort()
print('a1 :', a1)   # a1 : [3, 6, 9]
print('a2 :', a2)   # a2 : None
```



### `sorted(<list>)`

- 내장 함수 => 리스트 원본 값은 그대로이고, 정렬 값을 반환
- 원본 리스트 값은 유지되면서, 정렬된 새 리스트는 새로운 리스트에 저장

``` python
b1 = [6, 3, 9]
print('b1 :', b1)  # b1 : [6, 3, 9]
b2 = sorted(b1)
print('b1 :', b1)  # b1 : [6, 3, 9]
print('b2 :', b2)  # b2 : [3, 6, 9]
```

