
import random

from random import randint

def list_nums(nums):
    new_list = []
    for nums in range(int(input('Введите размер списка: '))):
        new_list.append(randint(1, 12))
    print(new_list)
    n = len(new_list)
    i = 0
    while i < n-1:
        j = i+1
        r = False
        while j < n:
            if new_list[j] == new_list[i]:
                new_list.pop(j)
                n -= 1
                r = True
            else:
                j += 1
        if r:
            new_list.pop(i)
            n -= 1
        else:
            i += 1

    print(new_list)


list_nums(' ')
