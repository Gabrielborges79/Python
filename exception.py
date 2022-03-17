
lista = [1, 10]
arquivo=open('teste.txt', 'r')
try:
    divisao = 10/1
    numero=lista[1]
    texto=arquivo.read()
    ##x = a

except ZeroDivisionError:
    print('Não é possivel dividir por 0')
except ArithmeticError:
    print('Houve um erro aritmetico')
except IndexError:
    print('erro ao Acessar um indice invalido')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre erro')
finally:
    print('Sempre Executa')
    print('Fechando arquvo')
    arquivo.close()