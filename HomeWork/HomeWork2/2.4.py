# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

num_list = []
a = int(input("range^ "))
for i in range(-a, a+1):
    num_list.append(i)
print(num_list)
possition1 = int(input("1^ "))
possition2 = int(input("2^ "))
if possition1 == 0 or possition2 == 0 or possition1 > a or possition2 > a:
    print("Одна из позиций = 0 или такой позиции не существует(")    
else:
    print(num_list[possition1 - 1] * num_list[possition2 - 1])

