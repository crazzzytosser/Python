# 1. Задайте список, состоящий из произвольных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# # 22

import random #(1-й способ(точечная нотация))
#from random import sample  #(2-й способ)56

def find_number (amount):
    new_list = random.sample(range(0, 100), k=amount)  #(k вплотную) (sample - возврящает список)
    print(new_list)
    list_lenght = len(new_list)
    sum = 0
    count = 0
    while count < list_lenght:
        sum += new_list[count]
        count += 2
    print(sum)

find_number(int(input('Введите количество символов: ')))

