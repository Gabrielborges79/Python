qtd = int(input())

for i in range(qtd):
    a, b = input().split()

    # Se os ultimos numeros de 'num1' foram iguais aos numeros componentes de 'num2'
    if b == a[len(a)-len(b):len(a)]:
        print('encaixa')
    else:
        print('nao encaixa')