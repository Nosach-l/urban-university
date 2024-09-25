data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    summ = 0
    for i in args:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            summ += calculate_structure_sum(*i)
        if isinstance(i, dict):
            summ += calculate_structure_sum(*i.keys()) + calculate_structure_sum(*i.values())
        elif isinstance(i, int):
            summ += i
        elif isinstance(i, str):
            summ += len(i)
    return summ


result = calculate_structure_sum(data_structure)
print(result)
