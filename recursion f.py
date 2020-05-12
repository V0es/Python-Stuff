def rec(n):
    a = n // 10
    f = n % 10
    print(f)
    if a >= 1:
        rec(a)
    else:
        return


num = int(input())
rec(num)
