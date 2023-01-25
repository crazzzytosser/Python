# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

nums = [i for i in range(20, int(input('Введите число больше 20: '))+1) if i % 20 == 0 or i % 21 == 0]
print(nums)