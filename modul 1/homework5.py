immutable_var = 1, 10, 'string', True  # immutable_var - кортеж
print(immutable_var)
# кортеж – это неизменяемая упорядоченная коллекция, которая может содержать в себе разные типы данных
mutable_list = [1, 10, "string", True]
print(mutable_list)
mutable_list[0] = 100
mutable_list[-1] = False
mutable_list.append("доска")
print(mutable_list)
