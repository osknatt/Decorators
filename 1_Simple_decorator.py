import datetime

def decor1(old_function):
    def new_function(*args, **kwargs):
        with open('logs.txt', 'w', encoding='utf-8') as outfile:
            outfile.write(str(datetime.datetime.now()))
            outfile.write(
                '\nБыла вызвана функция ' + old_function.__name__ + ' с аргументами ' + str(args if args else "") +
                str(kwargs if kwargs else ""))
            outfile.write('\nВозвращаемое значение: ' + old_function(*args, **kwargs))
    return new_function

@decor1
def test_foo(name, age):
    return f'Meet {name}, he/she is {age} y.o.'

test_foo('John', 30)
