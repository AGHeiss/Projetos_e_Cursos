"""
24 - Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com excessão dele próprio.
Ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
valor = int(input('Digite um número inteiro positivo: '))
divisores = []
for divisor in range(1, valor):
    if valor % divisor == 0:
        divisores.append(divisor)
print(divisores, sum(divisores))

25 - Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.
multiplos = []
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        multiplos.append(i)
print(sum(multiplos))

26 - Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
valor = int(input('Digite um número inteiro positivo: '))
print(f'Esse número é multiplo de 11, 13 ou 17?? Veja o resultado da divisão, respectivamente: {valor % 11}, {valor % 13}, {valor % 17}.')

27 - Em matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmônica:
H(n) = 1 + 1 / 2 + 1 / 3 + 1 / 4 + ... + 1 / n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
"""






