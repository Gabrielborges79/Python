import shutil

def escrever_arquivos(nome_arquivo):
   ## diretorio = 'C:/Users/JOSEBORGES/Documents/Python/ateste1.txt'
    arquivo = open ('notas.txt', 'w')
    arquivo.write(nome_arquivo)
    arquivo.close()

def atualizar_arquivo(nome_arquivo):
    arquivo=open('notas.txt', 'a')
    arquivo.write(nome_arquivo)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo=open(nome_arquivo, 'r')
    texto= arquivo.read()
    print(texto)

def media(nome_arquivo):
    arquivo =open('notas.txt', 'r')
    pass

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'C:/Users/JOSEBORGES/Documents/Python')

def move_arquivo(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo,'C:/Users/JOSEBORGES/Documents' )

if __name__ == '__main__':
    copia_arquivo('notas.txt')
    move_arquivo('notas.txt')
   ## escrever_arquivos('Primeira media')
