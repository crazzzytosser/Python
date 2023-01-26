# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open(input('file name1 '), 'w') as data:
    data.writelines(input('input the text1'))

with open(input('file name2 '), 'w') as data:
    data.writelines(input('input the text2 '))

read = input('file name read ')
data = open(read, 'r')
for i in data:
    print(i)

    file_in = open("INPUTFILE.txt", 'r')
    file_out = open("OUTFILE.txt", 'w')
    file_out.write(file_in.read())