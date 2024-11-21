"""
18 - Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo). O usuário escolhe uma das
opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo.
operacoes = input('Das 4 operações matemáticas básicas: Soma, subtração, multiplicação e divisão. Digite qual você gostaria de usar para cálculo: ')
operacoes = operacoes.title()
calculo = []

for i in range (1, 3):
    numeros = input(f'Digite o {i}º número para o cálculo de {operacoes}: ')
    try:
        numeros = float(numeros)
    except:
        print(f'Valor incorreto. Você digitou: {numeros}. Por favor use apenas números separados por ponto.')
        exit()
    calculo.append(numeros)
if operacoes == 'Soma':
    soma = calculo[0] + calculo[1]
    print(f'A soma: {calculo[0]} + {calculo[1]} é igual a {soma}.')
elif operacoes == 'Subtração':
    subtracao = calculo[0] - calculo[1]
    print(f'A subtração: {calculo[0]} - {calculo[1]} é igual a {subtracao}.')
elif operacoes == 'Multiplicação':
    multiplicacao = calculo[0] * calculo[1]
    print(f'A multiplicação: {calculo[0]} * {calculo[1]} é igual a {multiplicacao}.')
elif operacoes == 'Divisão':
    divisao = calculo[0] / calculo[1]
    print(f'A divisão: {calculo[0]} / {calculo[1]} é igual a {divisao}.')
else:
    print(f'Esses são os números que você digitou: {calculo}. Por favor escolha uma operação matemática básica entre: Soma, Subtração, Multiplicação ou Divisão.')

19 - Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou por 5, mas não simultaneamente pelos dois.
numero = input('Digite um número inteiro qualquer: ')
try:
    numero = int(numero)
except:
    print(f'Valor incorreto. Você digitou: {numero}. Por favor use apenas números inteiros. Exemplo: 5.')
    exit()
if numero % 3 == 0:
    print(f'O número {numero} é divisível por 3.')
elif numero % 5 == 0:
    print(f'O número {numero} é divisível por 5.')
else:
    print(f'O número {numero} não é divisível por 3 nem por 5.')

20 - Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um triângulo escaleno,
equilátero ou isósceles, considerando os seguintes conceitos:
- O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
- Chama-se equilátero o triângulo que tem três lados iguais
- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
- Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
numeros = []
for i in range(1, 4):
    triangulo = input(f'Digite o {i}º lado do triângulo: ')
    try:
        triangulo = float(triangulo)
    except:
        print(f'Valor incorreto. Você digitou: {triangulo}. Por favor use apenas números inteiros. Exemplo: 4.')
        exit()
    numeros.append(triangulo)
if numeros[0] < numeros[1] + numeros[2]:
    print(f'Esses valores formam um triângulo. Os lados dele valem: {numeros}.')
    if numeros[0] == numeros[1]:
        print('Esse é um triângulo isósceles, pois possui dois lados iguais.')
        if numeros[1] == numeros[2]:
            print('Esse é um triângulo equilátero. Pois possui três lados iguais.')
    if numeros[0] != numeros[1]:
        if numeros[1] != numeros[2]:
            print('Esse é um triângulo escaleno. Pois possui os três lados diferentes.')
else:
    print('Esses números não formam um triângulo')

21 - Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida.
numeros = []
for i in range(1, 3):
    numero = input(f'Digite o {i}º número inteiro: ')
    try:
        numero = float(numero)
    except:
        print(f'Valor incorreto. Você digitou: {numero}. Por favor use apenas números separados por ponto. Exemplo: 4.0')
        exit()
    numeros.append(numero)
opcao = input('Escolha a opção abaixo: \n'
      '1- Soma de 2 números. \n'
      '2- Diferença entre 2 números (maior pelo menor). \n'
      '3- Produto entre 2 números. \n'
      '4- Divisão entre 2 números (o denominador não pode ser zero).\n'
      '--> ')
try:
    opcao = int(opcao)
except:
    print(f'Valor incorreto. Você digitou: {opcao}. Por favor use apenas os números inteiros do menu.')
    exit()
if opcao == 1:
    soma = numeros[0] + numeros[1]
    print(f'Soma: {numeros[0]} + {numeros[1]} é igual a {soma}.')
elif opcao == 2:
    if numeros[0] >= numeros[1]:
        diferenca = numeros[0] - numeros[1]
        print(f'A diferença entre {numeros[0]} e {numeros[1]} é de {diferenca}')
    elif numeros[1] >= numeros[0]:
        diferenca = numeros[1] - numeros[0]
        print(f'A diferença entre {numeros[1]} e {numeros[0]} é de {diferenca}')
elif opcao == 3:
    produto = numeros[0] * numeros[1]
    print(f'O produto de {numeros[0]} * {numeros[1]} é igual a {produto}.')
elif opcao == 4:
    if numeros[1] == 0:
        print(f'O denominador não pode ser igual a 0. Tente outra opção.')
    else:
        divisao = numeros[0] / numeros[1]
        print(f'A divisão de {numeros[0]} por {numeros[1]} é igual a {divisao}.')
else:
    print(f'Você digitou uma opção inválida: {opcao}. Por favor tente novamente entre números de 1 a 4.')

22 - Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
As condições para aposentadoria são:
- Ter pelo menos 65 anos,
- Ou ter trabalhado pelo menos 30 anos,
- Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos
idade = input('Digite a sua idade: ')
try:
    idade = int(idade)
except:
    print(f'Valor incorreto. Você digitou: {idade}. Por favor use apenas números inteiros. Exemplo: 65')
    exit()
servico = input('Digite o seu tempo de serviço (anos trabalhados): ')
try:
    servico = int(servico)
except:
    print(f'Valor incorreto. Você digitou: {servico}. Por favor use apenas números inteiros. Exemplo: 30')
    exit()
if idade >= 65:
    print(f'Você já pode se aposentar pela sua idade.')
    if servico >= 30:
        print('Além disso você já tem mais de 30 anos de serviço.')
elif servico >= 30:
    print(f'Você já tem o tempo de serviço necessário para se aposentar.')
elif idade >= 60:
    if servico >= 25:
        print(f'Você já consegue se aposentar.')

23 - Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100.
Por exemplo: 1988, 1992, 1996
ano = input('Digite um ano, exemplo: 1982 \n'
            '--> ')
try:
    ano = int(ano)
except:
    print(f'Valor incorreto. Você digitou: {ano}. Por favor use apenas números inteiros: 1992')
    exit()
if ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
elif ano % 100 == 0:
    print(f'O ano {ano} não é bissexto!')
elif ano % 4 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')

24 - Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%;
RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço final do produto acrescido
do imposto do estado em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
estado = input('Digite um estado que comprará o produto: ')
estados = ['MS', 'MATO GROSSO DO SUL', 'SP', 'SÃO PAULO', 'RJ', 'RIO DE JANEIRO', 'MG', 'MINAS GERAIS']
estado = estado.upper()
if estado in estados:
    print(f'Você pode comprar o produto nesse estado.')
    preco = input('Informe o valor do produto (R$): ')
    try:
        preco = float(preco)
    except:
        print(f'Valor incorreto. Você digitou: {preco}. Por favor use apenas números separados por ponto. Exemplo: 1500.00')
        exit()
    if estado == 'MS':
        final = preco * 1.08
        print(f'Esse é o valor do produto no Mato Grosso do Sul: R${final}')
    elif estado == 'MATO GROSSO DO SUL':
        final = preco * 1.08
        print(f'Esse é o valor do produto no Mato Grosso do Sul: R${final}')
    elif estado == 'SP':
        final = preco * 1.12
        print(f'Esse é o valor do produto em São Paulo: R${final}')
    elif estado == 'SÃO PAULO':
        final = preco * 1.12
        print(f'Esse é o valor do produto em São Paulo: R${final}')
    elif estado == 'RJ':
        final = preco * 1.15
        print(f'Esse é o valor do produto no Rio de Janeiro: R${final}')
    elif estado == 'RIO DE JANEIRO':
        final = preco * 1.15
        print(f'Esse é o valor do produto no Rio de Janeiro: R${final}')
    elif estado == 'MG':
        final = preco * 1.07
        print(f'Esse é o valor do produto em Minas Gerais: R${final}')
    elif estado == 'MINAS GERAIS':
        final = preco * 1.07
        print(f'Esse é o valor do produto em Minas Gerais: R${final}')
else:
    print(f'Esse estado não está na lista de vendas de nossos produtos, você tem certeza que digitou corretamente? Você digitou: {estado!r}.')
"""








