"""
25 - Calcule as raízes da equação de 2º grau.
- A variável a tem que ser diferente de zero. Caso seja igual imprima a mensagem "Não é equação de segundo grau".
equacao = input(f"Digite a equação de 2º grau conforme o modelo: {' ax² + bx + c = 0'!r} \n"
                "--> ")
if equacao[0] == '-':
    a = equacao[0] + equacao[1]
else:
    a = equacao[1]
if equacao[5] == '-':
    b = equacao[5] + equacao[7]
else:
    b = equacao[7]
if equacao[10] == '-':
    c = equacao[10] + equacao[12]
else:
    c = equacao[12]
try:
    a = float(a)
    b = float(b)
    c = float(c)
except:
    print(f"Valor incorreto. Você digitou: {equacao}. Siga o exemplo:{' ax² + bx + c = 0'!r} ")
    exit()
delta = (b ** 2) - (4 * a * c)
raiz1 = (-b + delta) / 2 * a
raiz2 = (-b - delta) / 2 * a
print(f'O delta dessa equação é igual a: {delta}.')
if delta < 0:
    print('Não existe raiz.')
elif delta == 0:
    print(f'Raiz única. Raiz: {raiz1, raiz2}')
elif delta >= 0:
    print(f'As raízes são: x1: {raiz1} x2: {raiz2}')

26 - Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo
em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
distancia: str = input('Digite uma distância percorrida pelo seu automóvel: ')
try:
    distancia: float = float(distancia)
except:
    print(f'Valor incorreto. Você digitou: {distancia!r}. Por favor use apenas números separados por ponto. Exemplo: 500.0')
    exit()
litros: str = input('Digite a quantidade de litros gasto nessa viagem: ')
try:
    litros: float = float(litros)
except:
    print(f'Valor incorreto. Você digitou: {litros!r}. Por favor use apenas números separados por ponto. Exemplo: 50.0')
    exit()
rendimento = distancia / litros
if rendimento < 8:
    print('Venda o carro!')
elif rendimento > 8 and rendimento < 14:
    print('Econômico!')
elif rendimento > 12:
    print('Super econômico!')

27 - Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
idade: str = input('Digite a sua idade: ')
try:
    idade: int = int(idade)
except:
    print(f'Valor incorreto. Você digitou: {idade}. Por favor use apenas números inteiros. Exemplo: 5')
if idade >= 5 and idade <= 7:
    print(f"A sua categoria é 'Infantil A'.")
elif idade >= 8 and idade <= 10:
    print(f"A sua categoria é 'Infantil B'.")
elif idade >= 11 and idade <= 13:
    print(f"A sua categoria é 'Juvenil A'.")
elif idade >= 14 and idade <= 17:
    print(f"A sua categoria é 'Juvenil B'.")
elif idade >= 18:
    print(f"A sua categoria é 'Sênior'.")

28 - Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médias de acordo com um valor
numérico digitado pelo usuário:
import math
numeros = []
for i in range(1, 4):
    numero: str = input(f'Digite o {i}º valor dos 3 valores: ')
    try:
        numero: float = float(numero)
    except:
        print(f'Valor incorreto. Você digitou: {numero}. Por favor use apenas números separados por ponto. Exemplo: 5.5')
        exit()
    numeros.append(numero)
print(f'Agora escolha o tipo de média que você deseja calcular com esses três valores: \n'
      f'=== Opção 1: Geométrica === \n'
      f'=== Opção 2: Ponderada === \n'
      f'=== Opção 3: Harmônica === \n'
      f'=== Opção 4: Aritmética ===')
opcao: str = input('Digite a opção escolhida: ')
try:
    opcao: int = int(opcao)
except:
    print(f'Valor incorreto. Você digitou: {opcao}. Por favor use apenas números inteiros. Exemplo: 2.')
    exit()
if opcao == 1:
    media = (numeros[0] * numeros[1] * numeros[2]) ** (1/3)
    print(f'Valores: {numeros}.\n'
          f'Média geométrica: {media}.')
elif opcao == 2:
    media = (numeros[0] + (numeros[1] * 2) + (numeros[2] * 3)) / 6
    print(f'Valores: {numeros}.\n'
          f'Média ponderada: {media}.')
elif opcao == 3:
    media = 1 / ((1 / numeros[0]) + (1 / numeros[1]) + (1 / numeros[2]))
    print(f'Valores: {numeros}.\n'
          f'Média harmônica: {media}.')
elif opcao == 4:
    media = (numeros[0] + numeros[1] + numeros[2]) / 3
    print(f'Valores: {numeros}.'
          f'Média aritmética: {media}.')
else:
    print(f'Opção inválida. Por favor digite um número entre 1 e 4. Você digitou: {opcao}.')

29 - Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100. Escolha números aleatórios
entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b, onde a e b são os números aleatórios. Peça a resposta. Faça cinco perguntas
ao aluno, e mostre para ele as perguntas e as respostas corretas, além de quantas vezes o aluno acertou.
from random import randint
acertos: int = 0
for i in range(1, 6):
    a: int = randint(1, 51)
    b: int = randint(1, 51)
    print(f'{i}ª pergunta: Quanto é {a} + {b} = ??')
    resposta: str = input('Digite a resposta: ')
    try:
        resposta: int = int(resposta)
    except:
        print(f'Valor incorreto. Você digitou: {resposta}. Por favor use apenas números inteiros. Exemplo: 77.')
        exit()
    if resposta == (a + b):
        print(f'Parabens! Você acertou! {a} + {b} = {a + b}')
        acertos = acertos + 1
    else:
        print(f'Tente novamente. Você errou. {a} + {b} não é {resposta}. A resposta correta é {a + b}.')
print(f'Você terminou as 5 perguntas, você acertou {acertos} perguntas.')

30 - Faça um programa que receba três números e mostre-os em ordem crescente.
numeros = []
for i in range(1, 4):
    numero: int = int(input('Digite um número inteiro: '))
    numeros.append(numero)
print(numeros)
numeros = sorted(numeros)
print(f'Em ordem crescente os números são: {numeros}')

31 - Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre qual a classificação dessa pessoa.
altura: float = float(input('Digite a sua altura (m): '))
peso: float = float(input('Digite o seu peso (kg): '))

if altura < 1.20 and peso < 60:
    print('Você é da categoria A.')
elif altura < 1.20 and peso <= 90 >= 60:
    print('Você é da categoria D.')
elif altura < 1.20 and peso > 90:
    print('Você é da categoria G.')
elif 1.20 <= altura <= 1.70 and peso < 60:
    print('Você é da categoria B.')
elif 1.20 <= altura <= 1.70 and 60 <= peso <= 90:
    print('Você é da categoria E.')
elif 1.20 <= altura <= 1.70 and peso > 90:
    print('Você é da categoria H.')
elif altura > 1.70 and peso < 60:
    print('Você é da categoria C.')
elif altura > 1.70 and 60 <= peso <= 90:
    print('Você é da categoria F.')
elif altura > 1.70 and peso > 90:
    print('Você é da categoria I.')


"""






