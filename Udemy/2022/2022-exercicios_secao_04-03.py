"""
28 - Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
soma = 0
for i in range(1, 4):
    valor = input(f' Digite o {i}º valor: ')
    try:
        valor = float(valor)
    except:
        print(f'Você digitou {valor}. Por favor use apenas números separados por ponto. Exemplo: 2.0')
        exit()
    soma = (valor * valor) + soma
print(f'A soma dos quadrados dos três valores obtidos é de: {soma}')

29 - Leia quatro notas, calcule a média aritmética e imprima o resultado
soma = 0
for i in range(1, 5):
    notas = input(f'Informe a sua nota do {i}º bimestre: ')
    try:
        notas = float(notas)
    except:
        print(f'Valor incorreto. Você digitou {notas}. Por favor informe um número separado por ponto. Exemplo: 8.0')
        exit()
    soma = notas + soma
media = soma / 4
print(f'A média da sua nota é de {media}')

30 - Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares
real = input('Digite um valor que representa um valor em reais (R$): ')
cotacao_dolar = 5.20
try:
    real = float(real)
except:
    print(f'Valor incorreto. Você digitou {real}. Por favor use apenas números separados por ponto. Exemplo: 20.0')
dolar = real / cotacao_dolar
print(f'O valor que você digitou é de R${real}. Ele é equivalente a U${dolar}.')

31 - Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
numero = input('Digite um número inteiro qualquer: ')
try:
    numero = int(numero)
except:
    print(f'Valor incorreto. Você digitou {numero}, por favor digite apenas numeros inteiros. Exemplo: 4.')
    exit()
sucessor = numero + 1
antecessor = numero - 1
print(f'O sucessor do número que você digitou é {sucessor}, e o antecessor é {antecessor}')

32 - Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
numero = input('Digite um número: ')
try:
    numero = int(numero)
except:
    print(f'Valor incorreto. Você digitou {numero}. Por favor use apenas números inteiros. Exemplo: 20.')
    exit()
sucessor_triplo = numero * 3 + 1
antecessor_dobro = numero * 2 - 1
print(f'O valor que você digitou é {numero}. O sucessor do seu triplo é {sucessor_triplo}. O antecessor de seu dobro é {antecessor_dobro}.')

33 - Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.
quadrado = input('Digite um número que representa o valor do lado de um quadrado: ')
try:
    quadrado = float(quadrado)
except:
    print(f'Valor incorreto. Você digitou {quadrado}. Por favor use apenas números separados por ponto. Exemplo: 2.5')
    exit()
area_quadrado = quadrado * quadrado
perimetro_quadrado = quadrado * 4
print(f'O quadrado de lado {quadrado}. Tem uma área quadrada de {area_quadrado}. E um perímetro de {perimetro_quadrado}.')

34 - Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente. A área do círculo é pi * raio², considere pi = 3,141592.
raio = input('Digite um número que representa um raio de um círculo qualquer: ')
try:
    raio = float(raio)
except:
    print(f'Valor incorreto. Você digitou: {raio}. Por favor use apenas números separados por ponto. Exemplo: 7.5')
    exit()
area_circulo = math.pi * (raio * raio)
perimetro_circulo = 2 * math.pi * raio
print(f'Você digitou um raio de {raio}. A área desse círculo é de {area_circulo}. E o seu perímetro é de {perimetro_circulo}.')

35 - Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = math.sqrt( ( a * a ) + ( b * b ) ).
Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa operação.
soma = 0
for i in range(1, 3):
    cateto = input(f'Informe o valor do {i}º cateto: ')
    try:
        cateto = float(cateto)
    except:
        print(f'Valor incorreto. Você digitou: {cateto}. Por favor use apenas números separados por ponto. Exemplo: 3.0')
        exit()
    soma = (cateto * cateto) + soma

hipotenusa = math.sqrt(soma)
print(f'A hipotenusa dos catetos escolhidos é de {hipotenusa}.')

36 - Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um cilindro circular é calculado
por meio da seguinte fórmula: math.pi * (raio * raio) * altura, onde pi = 3,141592.
raio = input(f'Digite um número que representa o raio de um cilindro: ')
altura = input(f'Por favor digite um número que representa a altura do mesmo cilindro: ')
try:
    raio = float(raio)
    altura = float(altura)
except:
    print(f'Valor incorreto. Você digitou: {raio}. Por favor use apenas números separados por ponto. Exemplo: 4.0')
    print(f'Valor incorreto. Você digitou: {altura}. Por favor use apenas números separados por ponto. Exemplo: 4.0')
    exit()
volume = (raio * raio) * math.pi * altura
print(f'O cilindro que você digitou tem um raio de {raio} metros. Uma altura de {altura} metros, e um volume de {volume} m³')

37 - Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.
produto_preco = input(f'Digite um valor que representa um preço de produto: ')
try:
    produto_preco = float(produto_preco)
except:
    print(f'Valor incorreto. Você digitou: {produto_preco}. Por favor use somente números separados por ponto. Exemplo: 20.50')
    exit()
desconto = input(f'Qual é o desconto que será aplicada nesse preço informado? Exemplo: 12.0 (12% de desconto)')
try:
    desconto = float(desconto)
except:
    print(f'Valor incorreto. Você digitou: {desconto}. Por favor use apenas números separados por ponto. Exemplo: 12.0.')
    exit()
liquido = (1 - (desconto / 100)) * produto_preco
print(f'O preço do produto é de R${produto_preco}. O desconto que será aplicado é de {desconto}%. O valor final com o desconto aplicado é de R${liquido}.')

38 - Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.
salario = input(f'Digite um número que representa o salário mensal (R$) de um funcionário: ')
try:
    salario = float(salario)
except:
    print(f'Valor incorreto. Você digitou: {salario}. Por favor use apenas números separados por ponto. Exemplo: 1212.00')
    exit()
aumento = input('Digite a porcentagem do aumento que o funcionário vai receber no seu novo salário. Exemplo: 25.0 (25% de aumento)')
try:
    aumento = float(aumento)
except:
    print(f'Valor incorreto. Você digitou: {aumento}. Por favor use apenas números separados por ponto. Exemplo: 25.0')
    exit()
novo_salario = salario * (1 + aumento / 100)
print(f'O salário antigo do funcionário é de: R${salario}. O aumento que ele vai receber do salário é de {aumento}%. O seu novo salário será de R${novo_salario}.')

"""
import math



















