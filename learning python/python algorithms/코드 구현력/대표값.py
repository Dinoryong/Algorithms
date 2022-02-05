'''
파이썬 round 는 round-half-even 방

'''
a=4.5000
print(round(a))

a=66.6
a+0.5
a=int(a)
print(a)

def solution(n, a):
    ave = round(sum(a)/n)
    min=2147000000
    for idx, x in enumerate(a):
        tmp = abs(x-ave)
        if tmp<min:
            min = tmp
            score = x
            res = idx + 1
        elif tmp == min:
            if x>score:
                score=x
                res=idx+1