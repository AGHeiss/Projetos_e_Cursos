"""
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o python encontra um erro de sintaxe. Ou seja, você escreveu algo que o python não reconhece
como parte da linguagem.

# Exemplos SyntaxError
a)
def funcao:
    print('Geek University')

b)
None = 1

c)
return

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

# Exemplos NameError
a)
print(geek)

b)
geek()

c)
a = 18
if a < 10:
    msg = 'É maior que 10'

print(msg)

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

# Exemplos TypeError
a)
print(len(5))

b)
print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um
índice invalido

# Exemplos IndexError
a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[0][10])

5 - ValueError -> Ocorre quando uma função ou uma operação built-in (integrada) recebe um argumento
com tipo correto mas valor inapropriado

# Exemplos ValueError
a)
print(int('Geek'))

b)

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

# Exemplos KeyError
a)
dic = {}
print(dic['geek'])

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

# Exemplos AttributeError
a)
tupla = (11, 2, 31, 4)
print(tupla.sort())

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

# Exemplos IndentationError
a)
def nova():
print('Geek')

b)
for i in range(10):
i + 1

OBS: Exceptions e Erros são sinônimos na programação. Importante ler e prestar atenção na saída de erro.
"""

