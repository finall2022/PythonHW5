""" Реализуйте RLE алгоритм: реализуйте модуль 
сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах. """
path_in = 'task4file_c_in.txt'
path_out = 'task4file_c_out.txt'
data_in = open(path_in, 'r')
data_out = open(path_out, 'w')
line_out = ""

i = 0
j = 0

for line_in in data_in:
    while i < len(line_in):
        count = 1
        while i + 1 < len(line_in) and line_in[i] == line_in[i + 1]:
            count += 1
            i += 1

        line_out += str(count) + line_in[i]
        i += 1

data_out.write(line_out)
print(line_out)
data_in.close()
data_out.close()
