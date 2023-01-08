# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн
# in 54                           #in 9990                           # in 650
# out [2, 3, 3, 3]                #out [2, 3, 3, 3, 5, 37]          # out [2, 5, 5, 13]

def simple_factor(n):
    while n < 0:
        n = (abs(n))
    else:
        list = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                list.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            list.append(n)
            print(list)
        return list


simple_factor(int(input('Введите любое число: ')))
