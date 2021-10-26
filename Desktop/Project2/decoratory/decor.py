import datetime
import os

def decor_func(sample):

    def new_func(path, *args):
        # можно попросить пользователя указать путь к файлу: path = input('укажите путь к папке с логом: ')
        with open(f'{path}/log.txt', 'a') as log:
         log.write(f'{datetime.datetime.now().strftime("%d %b %Y, %H : %M : %S")} | ')
         log.write(f'{sample.__name__} | ')
         log.write(f'{args} | ')
         result = sample(path, *args)
         return log.write(f'{str(result)}\n')
    return new_func

@decor_func
def perimetr(file_path,a,b):
    return 2*(a+b)

if __name__ == '__main__':
    perimetr(os.getcwd(),2,3)