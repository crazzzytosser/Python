# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = input("Input the number: ")
sum = 0
step = len(num)
num = float(num)
num *= 10 ** step
while num > 0:
    sum += num % 10
    num //= 10
print(sum)