import random


def odd_nums(max_num):
    """НЕ используя слово ключевое yield"""
    return (random.randrange(1, max_num+1, 2) for _ in range(0, max_num))


odd_to_15 = odd_nums(15)
print('odd_nums(15):\n', *odd_to_15)

odd_to_20 = odd_nums(21)
print('\nodd_nums(21):\n', *odd_to_20)
