def solution(n,a):
    def digit_sum():
        sum = 0
        # while x > 0:
        #     sum += x % 10
        #     x = x // 10
        # return sum

        for i in str(x):
            sum += int(i)
        return sum

    max = -2147000000

    for x in a:
        tot = digit_sum(x)
        if tot > max:
            max = tot
            res = x
    print(res)