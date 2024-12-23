"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.

arquivo = open('2022-texto.txt')

print(arquivo.read())

# seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um parâmetro que indica
# onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek() -> Procurar

arquivo.seek(0)

print(arquivo.read())

arquivo.seek(19)

print(arquivo.read())


# readline() -> Função que lê o arquivo linha a linha (readline -> lê linha)

ret = arquivo.readline()

print(type(ret))

print(ret)

# readlines()

linhas = arquivo.readlines()

print(len(linhas))

OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador
e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão.
Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo;

# 1 - Abrir o arquivo;
arquivo = open('2022-texto.txt')

# 2 - Trabalhar o arquivo;
print(arquivo.read(100))

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo

print(arquivo.closed) # Verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo;
arquivo.close()

print(arquivo.closed) # Verifica se o arquivo está aberto ou fechado

# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError.
"""