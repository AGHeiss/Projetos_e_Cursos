"""
Generator Expression

Em aulas anteriores nós estudamos:
 - List Comprehension;
 - Dictionary Comprehension;
 - Set Comprehension;

 Não vimos:
 - Tuple Comprehension... porque elas se chamam Generators

 nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

 print(any([nome[0] == 'C' for nome in nomes]))

 # Poderíamos ter feiro utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator

res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string mais espaço ocupa.
print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(45645656456498821356))

print(getsizeof(True))


from sys import getsizeof

# Gerando uma lista de números com List Comprehension

list_comp = getsizeof([10 * x for x in range(1000)])

# Gerando uma lista de números com Set Comprehension

set_comp = getsizeof({10 * x for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension

dic_comp = getsizeof({x: 10 * x for x in range(1000)})

# Gerando uma lista de números com Generator

gen = getsizeof(10 * x for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

"""



