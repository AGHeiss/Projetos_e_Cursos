"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)
________________________
|Python|Módulos builtin|
------------------------

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

from random import randint as rdi, random as rdm

print(rdi(5, 81))
print(rdm())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *
# import random - DIFERENTE na utilização

print(random())

# Importando todo o módulo

import random

print(random.random())

# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(2, 3))
lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)
print(choice('University'))

https://docs.python.org/3/py-modindex.html
"""



