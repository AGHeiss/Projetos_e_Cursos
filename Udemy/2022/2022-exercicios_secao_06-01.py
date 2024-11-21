"""
1 - Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.
multiplo_3 = []
for i in range(1, 6):
    multiplo = i * 3
    multiplo_3.append(multiplo)
    print(multiplo)
print(f'Os 5 primeiros números múltiplos de 3 estão nesse conjunto: {multiplo_3}')

2 - Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira vez deve usar a estrutura de repetição for, a segunda while, e a
terceira do while.
for i in range(1, 4):
    for numero in range(1, 101):
        print(numero)

a = 0
while a < 100:
    a = a + 1
    print(a)

3 - Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela, iniciando em 10 e terminando em 0.
Mostrar uma mensagem "FIM!" após a contagem.
import time
a = 10
while a > -1:
    print(a)
    time.sleep(1)
    a = a - 1
print('FIM')

4 - Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em 1000, imprimindo seu valor na tela,
até que seu valor seja 100000 (cem mil).
a = 0
while a <= 100000:
    print(a)
    a = a + 1000

5 - Faça um programa que peça ao usuário para digitar 10 valores e some-os.
numeros = []
for i in range(1, 11):
    valor = float(input(f'Digite o {i}º valor: '))
    numeros.append(valor)
print(sum(numeros))

6 - Faça um programa que leia 10 inteiros e imprima sua média.
numeros = []
for i in range(1, 11):
    valor = float(input(f'Digite o {i}º valor: '))
    numeros.append(valor)
if i == 10:
    print(sum(numeros) / i)

7 - Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
numeros = []
for i in range(1, 11):
    valor = float(input(f'Digite o {i}º valor: '))
    if valor > 0:
        numeros.append(valor)
if i == 10:
    print(sum(numeros) / len(numeros))

8 - Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
numeros = []
for i in range(1, 11):
    valor = float(input(f'Digite o {i}º valor: '))
    numeros.append(valor)
print(f'O maior valor escrito é: {max(numeros)}')
print(f'O menor valor escrito é: {min(numeros)}')

9 - Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.
valor = int(input('Digite um valor qualquer: '))
for i in range(valor, valor + valor):
    if i % 2 == 0:
        continue
    print(i)

10 - Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
soma = []
for i in range(1, 300):
    if i % 2 != 0:
        continue
    soma.append(i)
    if len(soma) >= 50:
        break
print(soma)
print(sum(soma))

11 - Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente.
valor = int(input('Digite um número inteiro positivo qualquer: '))
numeros = []
for i in range(0, valor+1):
    numeros.append(i)
print(numeros[::1])

12 - Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente.
valor = int(input('Digite um número inteiro positivo qualquer: '))
numeros = []
for i in range(0, valor+1):
    numeros.append(i)
print(numeros[::-1])

13 - Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente.
valor = int(input('Digite um número inteiro qualquer: '))
numeros = []
for i in range(0, valor+1):
    if i % 2 != 0:
        continue
    numeros.append(i)
print(numeros[::1])

14 - Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente.
valor = int(input('Digite um número inteiro qualquer: '))
numeros = []
for i in range(0, valor+1):
    if i % 2 != 0:
        continue
    numeros.append(i)
print(numeros[::-1])

15 - Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1 até N em ordem crescente.
valor = int(input('Digite um número inteiro positivo qualquer: '))
numeros = []
for i in range(0, valor+1):
    if i % 2 == 0:
        continue
    numeros.append(i)
print(numeros[::1])

16 - Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1 até N em ordem decrescente.
valor = int(input('Digite um número inteiro positivo qualquer: '))
numeros = []
for i in range(0, valor+1):
    if i % 2 == 0:
        continue
    numeros.append(i)
print(numeros[::-1])

17 - Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais.
valor = int(input('Digite um número inteiro positivo: '))
numeros = []
for i in range(0, valor + 1):
    numeros.append(i)

print(sum(numeros))

18 - Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido.
A quantidade de números a serem lidos deve ser fornecida pelo usuário.
numeros = []
maiores = []
for i in range(1, 6):
    valor = int(input(f'Digite o {i}º valor: '))
    numeros.append(valor)

maior = max(numeros)
maiores.append(maior)
numeros.remove(maior)
maior2 = max(numeros)
if maior2 == maior:
    maiores.append(maior2)
    numeros.remove(maior2)
    maior3 = max(numeros)
    if maior3 == maior:
        maiores.append(maior3)
        numeros.remove(maior3)
        maior4 = max(numeros)
        if maior4 == maior:
            maiores.append(maior4)
            numeros.remove(maior4)
            maior5 = max(numeros)
            if maior5 == maior:
                maiores.append(maior5)
                numeros.remove(maior5)
print(f'O maior número é {maior}, ele foi repetido {len(maiores)} vezes.')

19 - Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos que compõem o número.
import random
numero = random.randint(100, 999)
numero = str(numero)
for algarismo in numero:
    print(algarismo)

20 - Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de dados
lidos e números de valores pares. O processo termina quando for digitado o número 1000.
pares = []
numeros = []
for i in range(1, 11):
    valor = int(input(f'Digite o {i}º número inteiro positivo: '))
    numeros.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    if valor == 1000:
        numeros.remove(1000)
        pares.remove(1000)
        break
print(f'Foram lidos {len(numeros)} números. Eles são: {numeros}\n'
      f'{len(pares)} desses números são pares. Eles são: {pares}.')

21 - Faça um programa que receba dois números. Calcule e mostre:
- a soma dos números pares desse intervalo de números, incluindo os números digitados;
- a multiplicação dos números ímpares desse intervalo, incluindo os digitados;

numeros = []
pares = []
impares = []
for i in range(1, 3):
    valor = int(input(f'Digite o {i}º valor inteiro positivo: '))
    numeros.append(valor)
if numeros[0] > numeros[1]:
    for numero in range(numeros[1], numeros[0]+1):
        if numero % 2 == 0:
            pares.append(numero)
        elif numero % 2 != 0:
            impares.append(numero)
elif numeros[1] > numeros[0]:
    for numero in range(numeros[0], numeros[1]+1):
        if numero % 2 == 0:
            pares.append(numero)
        elif numero % 2 != 0:
            impares.append(numero)
print(pares)
print(sum(pares))
print(impares)
produto = 1
for n in impares:
    produto = produto * n
print(produto)

22 - Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,uma sequência arbitrária de notas
(válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente média aritmética. O número de notas
com que o aluno pretenda efetuar o cálculo não será fornecido ao programa, o qual terminará quando for introduzido um valor
que não seja válido como nota de aprovação
numeros = []
for n in range(1, 11):
    valor = int(input(f'Digite a {n}ª nota, um valor entre 10 e 20: '))
    if 10 <= valor <= 20:
        numeros.append(valor)
        print(f'Você digitou {len(numeros)} notas. A média é {sum(numeros) / len(numeros)}.')
    else:
        print('Valor incorreto.')
        break

23 - Faça um algoritmo que leia um número positivo e imprima seus divisores.
valor = int(input('Digite um número inteiro positivo: '))
divisor = []
for divisores in range(1, valor+1):
    if valor % divisores == 0:
        divisor.append(divisores)
print(f'Os divisores de {valor} são: {divisor}.')
"""



















