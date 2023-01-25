# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.



# list = [int(s) for s in input().split() \
#         for i in range(1, len(list)) if list[i] > list[i-1]]
# print(list)


# res = [int(s) for s in input().split() for i in range(1, len(s)) if s[i] > s[i-1]]
# print(res)
list = [int(i) for i in input().split()]
res = [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]
print(res)