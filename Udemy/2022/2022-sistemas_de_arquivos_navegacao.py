"""
Sistemas de arquivos e navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

os -> Operating System - Sistema Operacional

# Fazer o import

import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd()) # C:\\Users\\Augusto\\PycharmProjects\\guppe

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')
print(os.getcwd()) # C:\\Users\\Augusto\\PycharmProjects

os.chdir('..')
print(os.getcwd()) # C:\\Users\\Augusto

os.chdir('..')
print(os.getcwd()) # C:\\Users

os.chdir('..')
print(os.getcwd()) # C:\\

# Podemos checar se um diretório é absoluto ou relativo
# OBS para usuários Windows
# Se você, infelizmente, estiver utilizando um computador com Windows,
# terá que ter cuidado ao verificar diretórios.
print(os.path.isabs('C:\\Users\\Augusto'))


# Podemos identificar o sistema operacional com o módulo os

print(os.name) # nt Windows


# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir())

# Fazer o import

import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

print(list(os.scandir()))
"""

