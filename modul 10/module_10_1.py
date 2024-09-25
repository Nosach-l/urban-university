from time import sleep
from datetime import datetime
from threading import Thread


time_start = datetime.now()


def write_words(word_count, file_name):
    file = open(file_name, "w", encoding="utf-8")
    for i in range(1, word_count+1):
        file.write(f'Какое-то слово № {i}' + '\n')
        sleep(0.1)
    file.flush()
    file.close()
    print(f'Завершилась запись в файл {file_name}')


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_elapsed = time_end - time_start
print(f'Работа потоков {time_elapsed}')

time_start = datetime.now()

first = Thread(target=write_words, args=(10, 'example5.txt'))
second = Thread(target=write_words, args=(30, 'example6.txt'))
third = Thread(target=write_words, args=(200, 'example7.txt'))
fourth = Thread(target=write_words, args=(100, 'example8.txt'))

first.start()
second.start()
third.start()
fourth.start()

first.join()
second.join()
third.join()
fourth.join()

time_end = datetime.now()
time_elapsed = time_end - time_start

print(f'Работа потоков {time_elapsed}')
