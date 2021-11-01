import datetime
import os

def paramtrized_decor(path):

    def decor_func(sample):

        def new_func(*args):
            with open(f'{path}/log.txt', 'a') as log:
             log.write(f'{datetime.datetime.now().strftime("%d %b %Y, %H : %M : %S")} | ')
             log.write(f'{sample.__name__} | ')
             log.write(f'{args} | ')
             result = sample(*args)
             log.write(f'{str(result)}\n')
             return result
        return new_func
    return decor_func

@paramtrized_decor(path=os.getcwd())
def perimetr(a,b):
    return 2*(a+b)


if __name__ == '__main__':
    print(perimetr(2,3))