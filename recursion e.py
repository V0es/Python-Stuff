i = 0


def rec(n, fin):
    fin += n % 10
    a = n // 10
    if a >= 1:
        rec(a, fin)
    else:
        print(fin)
        return


num = int(input())
rec(num, i)
