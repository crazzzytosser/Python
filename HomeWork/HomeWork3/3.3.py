# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def bin_num(num):
    num_list = []
    while num > 0:
        num_list.insert(0, num % 2)
        num //= 2  
    print(*num_list)
bin_num(int(input("Input your number: ")))