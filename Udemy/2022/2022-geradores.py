"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras
- Funções geradoras utilizam a palavra reservada yield
- Generators podem ser criados com Expressões Geradoras

Diferenças entre funções e generator functions (Funções geradoras)

--------------------------------------------------------------------------------------------
| Funções                                       | Generator Functions                       |
--------------------------------------------------------------------------------------------
| utilizam return                               | utilizam yield                            |
--------------------------------------------------------------------------------------------
| retorna uma vez                               | podem utilizar yield múltiplas vezes      |
--------------------------------------------------------------------------------------------
| quando executada, retorna um valor            | quando executada, retorna um generator    |
--------------------------------------------------------------------------------------------

# Exemplo de Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma generator function não é um generator. Ela gera um generator, ok?

gen = conta_ate(5)

# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)

for num in gen:
    print(num)

"""



