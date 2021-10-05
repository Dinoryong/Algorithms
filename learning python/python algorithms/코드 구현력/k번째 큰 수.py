'''
set()
- 자료구조는 중복을 제거해준다
- append가 아니라 add를 해줘야한다
- set 자료구조에는 sort 개념이 없. 즉, list화 시켜서 sort 작업 해야한다
'''


def solution(n, k, a):
    res = set() # set()은 중복을 제거하는 자료형
    for i in range(n):
        for j in range(i+1, n):
            for m in range(j+1, n):
                res.add(a[i]+a[j]+a[m])
    res = list(res)
    res.sort(reverse=True)
    print(res[k-1])





