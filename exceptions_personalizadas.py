class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x =int( input('Entre com um numero de 0 a 10: '))
        print(x)
        if x >10 or x<0:
            raise InputError('Nota não pode ser maior que 10 ou menor que 0')
        break
    except ValueError:
        print('Valor invalido. Digite um numero')
    except InputError as ex:
        print(ex)


