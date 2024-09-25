first_number = input("Здравствуйте, введите первое число: ")
second_number = input("введите второе число: ")
third_number = input("введите третье число: ")
if first_number == second_number == third_number:
    print(3)
elif first_number == second_number or first_number == third_number or second_number == third_number:
    print(2)
else:
    print(0)
