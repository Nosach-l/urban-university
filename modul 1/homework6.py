my_dict = {'Мелания': 2021, 'Ева': 1997, 'Нина': 1991}
print(my_dict)
print('существующий ключ:', my_dict['Нина'])
print('отсутствующий ключ:', my_dict.get('Vasia'))
my_dict.update({'Лев': 2023, 'Валера': 1986})
deleted_value = my_dict.pop('Ева')
print('Удаленное значение:', deleted_value)
print(my_dict)
my_set = {1, 'Яблоко', 1, 'Яблоко', 42.314, 42.314}
print('set:', my_set)
my_set.remove('Яблоко')
my_set.add((1, 2, 3))
my_set.add(50)
print('new set:', my_set)
