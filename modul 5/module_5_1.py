class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'"{self.name}" Такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(f'{self.name} мы на {floor + 1} этаже, Поднимаемся на {new_floor}-й этаж')


