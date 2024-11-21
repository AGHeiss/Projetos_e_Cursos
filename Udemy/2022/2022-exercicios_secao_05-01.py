"""
1 - Faça um programa que receba dois números e mostre qual deles é o maior.
numeros = []
for i in range(1, 3):
    numero = input('Digite um número qualquer: ')
    try:
        numero = float(numero)
    except:
        print(f'Valor incorreto. Você digitou: {numero}. Por favor use apenas números separados por ponto. Exemplo 5.0')
        exit()
    numeros.append(numero)
if numeros[0] > numeros[1]:
    print(f'{numeros[0]} é maior do que {numeros[1]}.')
elif numeros[0] == numeros[1]:
    print(f'{numeros[0]} é igual a {numeros[1]}.')
else:
    print(f'{numeros[1]} é maior do que {numeros[0]}.')

2 - Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem
dizendo que o número é inválido.
import math

numero = input(f'Digite um número qualquer: ')
try:
    numero = float(numero)
except:
    print(f'Valor incorreto. Você digitou: {numero}. Por favor use apenas números inteiros ou separados por ponto. Exemplo: 5.5')
    exit()
if numero >= 0:
    raiz = math.sqrt(numero)
    print(f'A raiz quadrada do número que você digitou é de {raiz}.')
else:
    print(f'Número inválido.')

3 - Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o numero ao quadrado.
import math
numero = input(f'Digite um número qualquer: ')
try:
    numero = float(numero)
except:
    print(f'Valor incorreto. Você digitou: {numero}. Por favor use apenas números inteiros ou separados por ponto. Exemplo: 5.5')
    exit()
if numero >= 0:
    raiz = math.sqrt(numero)
    print(f'A raiz quadrada do valor que você digitou é {raiz}.')
else:
    quadrado = numero ** 2
    print(f'O quadrado do número que você digitou é {quadrado}')

4 - Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
 - O número digitado ao quadrado
 - A raiz quadrada do número digitado
import math
numero = input(f'Digite um número qualquer: ')
try:
    numero = float(numero)
except:
    print(f'Valor incorreto. Você digitou: {numero}. Por favor use apenas números inteiros ou separados por ponto. Exemplo: 5.5')
    exit()
if numero >= 0:
    raiz = math.sqrt(numero)
    quadrado = numero ** 2
    print(f'O quadrado do número digitado é {quadrado}. E a raiz quadrada dele é {raiz}.')
else:
    print(f'Por favor use apenas números positivos. Você digitou: {numero}')

5 - Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.
numero = input(f'Digite um número qualquer: ')
try:
    numero = int(numero)
except:
    print(f'Valor incorreto. Você digitou: {numero}. Por favor use apenas números inteiros. Exemplo: 5')
    exit()
if numero % 2 == 0:
    print('Esse número é par.')
else:
    print('Esse número é impar.')

6 - Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
numeros = []
for i in range(1, 3):
    numero = input('Digite um número qualquer: ')
    try:
        numero = float(numero)
    except:
        print(f'Valor incorreto. Você digitou: {numero}. Por favor use apenas números inteiros ou separados por pontos. Exemplo: 4.5')
        exit()
    numeros.append(numero)
if numeros[0] > numeros[1]:
    diferenca = numeros[0] - numeros[1]
    print(f'{numeros[0]} é maior que {numeros[1]}. A diferença entre eles é {diferenca}')
elif numeros[0] == numeros[1]:
    print(f'{numeros[0]} é igual a {numeros[1]}.')
else:
    diferenca = numeros[1] - numeros[0]
    print(f'{numeros[1]} é maior que {numeros[0]}. A diferença entre eles é {diferenca}')

7 - Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem Números iguais.
numeros = []
for i in range(1, 3):
    numero = input('Digite um número qualquer: ')
    try:
        numero = float(numero)
    except:
        print(f'Valor incorreto. Você digitou: {numero}. Por favor use apenas números separados por ponto. Exemplo 5.0')
        exit()
    numeros.append(numero)
if numeros[0] > numeros[1]:
    print(f'{numeros[0]} é maior do que {numeros[1]}.')
elif numeros[0] == numeros[1]:
    print(f'Números iguais.')
else:
    print(f'{numeros[1]} é maior do que {numeros[0]}.')

8 - Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota válida deve ser,
obrigatoriamente, um valor entre 0,0 e 10,0 onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.
notas = []
for i in range(1, 3):
    numeros = input(f'Digite a sua {i}ª nota de 0 a 10: ')
    try:
        numeros = float(numeros)
    except:
        print(f'Valor incorreto. Você digitou: {numeros}. Use apenas números separados por ponto. Exemplo: 5.5')
    notas.append(numeros)
media = (notas[0] + notas[1]) / 2
if notas[0] >= 0:
    if notas[0] <= 10:
        if notas[1] >= 0:
            if notas[1] <= 10:
                print(f'O valor da sua média é de {media}.')
            else:
                print(f'Você digitou uma nota inválida: {notas}')
        else:
            print(f'Você digitou uma nota inválida: {notas}')
    else:
        print(f'Você digitou uma nota inválida: {notas}')
else:
    print(f'Você digitou uma nota inválida: {notas}')

9 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima:
Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
salario = input('Digite um valor que representa o salário mensal (R$) de uma pessoa: ')
try:
    salario = float(salario)
except:
    print(f'Valor incorreto. Você digitou: {salario}. Use apenas números separados por ponto. Exemplo: 1212.00')
    exit()
prestacao = input('Digite um valor que representa o valor da prestação (R$) de um empréstimo: ')
try:
    prestacao = float(prestacao)
except:
    print(f'Valor incorreto. Você digitou: {salario}. Use apenas números separados por ponto. Exemplo: 212.00')
    exit()

if prestacao >= (salario * 0.2):
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')

10 - Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
- Homens: (72.7 * h) - 58
- Mulheres: (62.1 * h) - 44.7
genero = input('Digite seu gênero (homem ou mulher): ')
genero = genero.title()
if genero == 'Homem':
    altura = input('Digite a sua altura com números separados por ponto, exemplo: 1.75 ->')
    try:
        altura = float(altura)
    except:
        print(f'Valor incorreto. Você digitou: {altura}. Por favor use apenas números separados por ponto. Exemplo: 1.65.')
        exit()
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é de {peso_ideal}kg')
elif genero == 'Mulher':
    altura = input('Digite a sua altura com números separados por ponto, exemplo: 1.75 ->')
    try:
        altura = float(altura)
    except:
        print(
            f'Valor incorreto. Você digitou: {altura}. Por favor use apenas números separados por ponto. Exemplo: 1.65.')
        exit()
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é de {peso_ideal}kg')
else:
    print('Gênero inválido. Por favor digite homem ou mulher.')
"""




