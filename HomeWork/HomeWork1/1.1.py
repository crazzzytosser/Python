# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input("Введите день недели: "))
if day > 7 and day != 0:
    print("Такого дня недели не существует((")
elif day == 6 or day == 7:
    print("Это выходной день!")
else:
    print("Это будний день!")
