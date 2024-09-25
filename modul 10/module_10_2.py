from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print('Knight ' + self.name + ' is under attack...')
        army_counter = 100
        days_counter = 0
        while army_counter > 0 if self.power > 0 else 0:
            army_counter -= self.power
            days_counter += 1
            sleep(1)
            print(f'{self.name} сражается {days_counter}..., осталось {army_counter} воинов.')
        return print(f'{self.name} одержал победу спустя {days_counter} дней(дня)!')


first_knight = Knight('пидор', 10)
second_knight = Knight('Sir Galahad', 20)
third_knight = Knight('Sir pidor', 30)


first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')






