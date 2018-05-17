# 5! = 120
#
# 5 * 4 * 3 * 2 * 1


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(f'5!={factorial(5):,},'  # 120
      f' 3!={factorial(3):,},'  # 6 
      f' 11!={factorial(11):,}')  # HUGE
