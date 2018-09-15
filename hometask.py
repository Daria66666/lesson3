def task1(sym):
    if ord(sym.lower()) >= 97 and ord(sym.lower()) <= 122:
        return True
    else:
        return False


def task2(number):
    try:
        if number < 0 or type(number) == float:
            raise ValueError
    except ValueError:
        print("Неправильный ввод")
    else:
        fact = 1
        if number == 0:
            return fact
        else:
            for i in range(1, number+1):
                fact *= i
            return fact


def task3():
    for a in range(1, 10):
        print("""
Умножение на """, a, ":")
        for b in range(1, 10):
            print(b, 'x', a, '=', b*a)