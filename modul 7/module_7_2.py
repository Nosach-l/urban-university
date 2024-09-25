def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='UTF-8')
    for i in range(0, len(strings)):
        strings_positions[(i + 1, file.tell())] = strings[i]
        file.write(str(strings[i]) + '\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test_file.txt', info)
for elem in result.items():
    print(elem)

