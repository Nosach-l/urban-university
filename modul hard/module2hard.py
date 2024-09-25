n = int(input('Введите число: '))
key = []
string = ''

for i in range(1, n):
    for j in range(1, n):
        if n % (i + j) == 0 and i > j and (i, j) not in key and (j, i) not in key:
            key.append(str(j) + str(i))
for el in key:
    string += el

print('ответ: ', string)
