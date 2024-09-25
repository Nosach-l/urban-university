from math import pi as pi


class Figure:
    sides_count = 0
    filled = False

    def __init__(self, color,  *sides):
        self.__sides = list(sides)
        self.__color = list(color)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return (all(isinstance(x, int) for x in (r, g, b))
                and all(0 <= x <= 255 for x in (r, g, b)))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *args):
        return (all(isinstance(x, int) for x in args)
                and all(0 < x for x in args)
                and len(args) == len(self.__sides))

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        perimeter = 0
        for i in range(0, len(self.__sides)):
            perimeter += self.__sides[i]
        return perimeter


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if len(list(sides)) != self.sides_count:
            self.set_sides(1)
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) == 1 and 0 not in sides:
            sides = (sides[0],) * self.sides_count
        elif len(sides) != self.sides_count:
            sides = [1] * self.sides_count

        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2

        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1 and 0 not in sides:
            sides = (sides[0],) * self.sides_count
        else:
            sides = (1,) * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

#  Проверка периметра (круга), это и есть длина:
print(len(circle1))

#  Проверка объёма (куба):
print(cube1.get_volume())
