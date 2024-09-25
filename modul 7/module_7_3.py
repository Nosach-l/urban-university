class WordsFinder:
    def __init__(self, *args):
        self.file_names = [*args]

    #  Создайте пустой словарь all_words.
    # Переберите названия файлов и открывайте каждый из них, используя оператор with.
    # Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
    # Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
    # (тире обособлено пробелами, это не дефис в слове).
    # Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
    # В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                string = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ', ', '. ', ' = ', '! ', '? ', '; ', ': ', ' - ']:
                    string = string.replace(i, ' ')
                all_words[file_name] = string.split()
        return all_words

    # find(self, word) - метод, где word - искомое слово. Возвращает словарь,
    # где ключ - название файла,
    # значение - позиция первого такого слова в списке слов этого файла.

    def find(self, word):
        for names, words in self.get_all_words().items():
            if word.lower() in words:
                index = words.index(word.lower()) + 1
                return {names: index}

    # count(self, word) - метод, где word - искомое слово.
    # Возвращает словарь, где ключ - название файла,
    # значение - количество слова word в списке слов этого файла.

    def count(self, word):
        for names, words in self.get_all_words().items():
            if word.lower() in words:
                index = words.count(word.lower())
                return {names: index}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
