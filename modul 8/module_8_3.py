class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model

        def __is_valid_vin(vin_number):
            if not isinstance(vin_number, int):
                raise IncorrectVinNumber(f"Некорректный тип vin номер: {vin_number}")
            elif vin_number < 1000000 or vin_number > 9999999:
                raise IncorrectVinNumber(f'Неверный диапазон для vin номера: {vin_number}')
            else:
                return True

        def __is_valid_numbers(numbers):
            if not isinstance(numbers, str):
                raise IncorrectCarNumbers(f'Некорректный тип данных для номеров: {numbers}')
            elif len(numbers) != 6:
                raise IncorrectCarNumbers(f'Неверная длина номера: {numbers}')
            else:
                return True

        self.__vin = __is_valid_vin(__vin)
        self.__numbers = __is_valid_numbers(__numbers)


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
