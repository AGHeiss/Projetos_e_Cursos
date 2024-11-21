"""
Sistemas de arquivos - Manipulação

import os
# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('arquivo.txt')) # False

# Diretório - relativos ou absolutos
print(os.path.exists('C:\\Users\\Augusto\\PycharmProjects\\guppe')) # True

# Criando arquivos ou diretórios
# diretórios
os.mkdir('teste')

# Renomear arquivos e diretórios

os.rename('2022-texto4', '2022-texto.txt')

#Removendo arquivos
os.remove('2022-texto3.txt')

# Removendo diretórios vazios
os.rmdir('teste')

# Podemos remover uma árvore de diretórios vazios ou criar árvore de diretórios
os.makedirs('teste\\outro\\geek')

os.removedirs('teste\\outro\\geek')

https://docs.python.org/3/library/os.html?highlight=os#module-os

"""

