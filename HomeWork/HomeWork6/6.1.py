# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.

list = [int(i) for i in input().split()]
res = [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]
print(res)