a, b, c = 'A', 'B', 'C'


def one(atr1):
    res1 = atr1 + '1'
    return res1


def two(atr2):
    res2 = atr2 + '2'
    return res2


def three(atr3):
    res3 = atr3 + '3'
    return res3


get1 = one(a)
get2 = two(b)
get3 = three(c)
lst = [get1, get2, get3]

for i in lst:
    print(i)
