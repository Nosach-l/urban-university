from time import sleep
from threading import Thread
import queue
import random


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            guest_table = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest_table = True
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    sleep(0.5)
                    break
            if not guest_table:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
                sleep(0.5)

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    sleep(0.5)
                    table.guest = None

                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        table.guest.start()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        sleep(0.5)

# Создание столов


tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
