
def add_two(x):
    return x + 2

def calculate_two(eq: str):
    first, sym, snd = eq.split()
    try:
        first, snd = int(first), int(snd)
    except ValueError:
        print("Формат ввода: VALUE1 <+-*/> VALUE2\n\
            Пример: 1 * 2")
    else:
        if sym == '+':
            return first + snd
        elif sym == '-':
            return first - snd
        elif sym == '*':
            return first * snd
        elif sym == '/':
            return first / snd

print(calculate_two('3 / 2'))

def return_from_list(index):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return nums[index]

def division(arg1, arg2):
    return arg1 / arg2

def file_1(name_1):
    with open(name_1, 'r') as file:
        list_from_file = file.readlines()
    dict_file = {}
    for line in list_from_file:
        key, value = line.split('=')
        v = int(value)
        dict_file [key] = value
    return dict_file

print(file_1('file_test.txt'))