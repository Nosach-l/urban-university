from threading import Thread, Lock
import random
import time


class Bank:
    def __init__(self):
        self.lock = Lock()
        self.balance = 0

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            else:
                amount = random.randint(50, 500)
                self.balance += amount
                print(f'Пополнение: {amount}. Баланс: {self.balance}', end='\n')
            time.sleep(0.1)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос: {amount}', end='\n')
            if amount > self.balance:
                print(f'Запрос отклонён, недостаточно средств', end='\n')
                self.lock.acquire()
            else:
                self.balance -= amount
                print(f'Снятие: {amount}. Баланс: {self.balance}', end='\n')


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
