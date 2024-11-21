"""
Teste de memória com Generators

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...


def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Teste 1
for n in fib_list(100000):
    print(n)


# Função usando geradores

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# Teste 2 usando geradores

for n in fib_gen(10000):
    print(n)

"""
