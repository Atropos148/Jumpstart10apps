# Fibonacci numbers
# 1, 1, 2, 3, 5, 8, 13, 21, ...


def fibonacci(limit):
    nums = []
    currnum = 0
    nextnum = 1

    while currnum < limit:
        currnum, nextnum = nextnum, nextnum + currnum
        nums.append(currnum)
    return nums


print('via lists')
for n in fibonacci(100):
    print(n, end=', ')

print()


def fibonacci_co():
    currnum = 0
    nextnum = 1

    while True:
        currnum, nextnum = nextnum, nextnum + currnum
        yield currnum


print('via yield')
for n in fibonacci_co():
    if n > 5000:
        break
    print(n, end=', ')
