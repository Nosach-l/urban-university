count = 0


def count_calls():
    global count
    count += 1


def string_info(string):
    a = str(string)
    a_new = (len(a), a.upper(), a.lower())
    count_calls()
    return a_new


def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            a = True
            break
        else:
            a = False
            continue
    return a


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(count)
