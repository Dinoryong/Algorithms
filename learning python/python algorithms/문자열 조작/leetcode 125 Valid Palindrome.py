def solution(n, s):
    for i in range(n):
        s = input()
        s = s.upper()
        size = len(s)
        print(s[-1])
        for j in range(size//2):
            if s[j] != s[-1-j]:
                print("NO")
                break
        print("YES")


