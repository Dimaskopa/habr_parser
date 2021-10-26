import datetime
import os

def decor_func(sample):

    def new_func(*args):
        # можно попросить пользователя указать путь к файлу: path = input('укажите путь к папке с логом: ')
        path = os.getcwd()
        with open(f'{path}/log.txt', 'a') as log:
         log.write(f'{datetime.datetime.now().strftime("%d %b %Y, %H : %M : %S")} | ')
         log.write(f'{sample.__name__} | ')
         log.write(f'{args} | ')
         result = sample(*args)
         return log.write(f'{str(result)}\n')
    return new_func


@decor_func
def summer(a,b,c):
    result = a+b+c
    return result

summer(1,2,3)