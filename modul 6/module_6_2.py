class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__color = str(__color)
        self.__engine_power = int(__engine_power)

    # Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
    # Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
    # Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
    # Метод print_info - распечатывает результаты методов (в том же порядке):
    # get_model, get_horsepower, get_color;
    # а так же владельца в конце в формате "Владелец: <имя>"

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}')

    # Метод set_color - принимает аргумент new_color(str),
    # меняет цвет __color на new_color, если он есть в списке
    # __COLOR_VARIANTS, в противном случае выводит на экран надпись:
    # "Нельзя сменить цвет на <новый цвет>"

    def set_color(self, new_color):
        if str(new_color).lower() in [colour.lower() for colour in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на новый {new_color}. ')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()