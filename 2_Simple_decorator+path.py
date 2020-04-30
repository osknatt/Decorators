import datetime
import os

def parametrized_decor1(path):
    def decor1(old_function):
        def new_function(*args, **kwargs):
            full_path = os.path.join(path, 'logs.txt')
            with open(full_path, 'w', encoding='utf-8') as outfile:
                outfile.write(str(datetime.datetime.now()))
                outfile.write(
                    '\nБыла вызвана функция ' + old_function.__name__ + ' с аргументами ' + str(args if args else "") +
                    str(kwargs if kwargs else ""))
                outfile.write('\nВозвращаемое значение: ' + old_function(*args, **kwargs))
        return new_function
    return decor1

@parametrized_decor1(path=r'C:\Users\natal\Desktop\Python\Advanced_Python\04_Decorators')
def test_foo(name, age):
    return f'Meet {name}, he/she is {age} y.o.'

test_foo('John', 30)