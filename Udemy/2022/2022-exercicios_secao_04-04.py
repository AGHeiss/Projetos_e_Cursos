"""
39 - A importância de R$780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:
- O primeiro ganhador receberá 46%
- O segundo receberá 32%
- O terceiro receberá o restante
Calcule e imprima a quantia ganha por cada um dos ganhadores.
premio_reais = 780000
primeiro_lugar = 0.46
segundo_lugar = 0.32
terceiro_lugar = 0.22
print(f'O prêmio total para os três primeiros lugares é de R${premio_reais}. O primeiro lugar ganhou {premio_reais * primeiro_lugar}. O segundo lugar ganhou '
      f'{premio_reais * segundo_lugar} e o terceiro lugar ganhou {premio_reais * terceiro_lugar}.')

40 - Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida
que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda
dias = input(f'Digite o número de dias trabalhados: ')
try:
    dias = float(dias)
except:
    print(f'Valor incorreto. Você digitou: {dias}. Por favor use apenas números separados por ponto. Exemplo: 20.0')
    exit()
salario = 30.0 * dias * 0.92
print(f'Sabendo que você ganha R$30,00 por dia. Você irá receber R${salario}.')

41 - Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário,
adicionando 10% sobre o valor calculado.
horas = input(f'Digite um número que representa o valor em reais(R$) a ser pago por hora: ')
try:
    horas = float(horas)
except:
    print(f'Valor incorreto. Você digitou: {horas}. Por favor use apenas números separados por ponto. Exemplo: 10.0')
    exit()
trabalho = input(f'Digite a quantidade de horas trabalhadas no mês: ')
try:
    trabalho = float(trabalho)
except:
    print(f'Valor incorreto. Você digitou: {trabalho}. Por favor use apenas números separados por ponto. Exemplo: 100.0')
    exit()
salario = (horas * trabalho) * 1.10
print(f'Você trabalhou {trabalho} horas. Recebendo R${horas} por hora. Seu salário será de R${salario}.')

42 - Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base.
Além disso, ele paga 7% de imposto sobre o salário-base.
salario = input(f'Digite o salário(R$) base que você irá receber: ')
try:
    salario = float(salario)
except:
    print(f'Valor incorreto. Você digitou: {salario}. Por favor use apenas números separados por ponto. Exemplo: 1212.0')
    exit()
imposto = salario * 0.07
salario_receber = (salario * 1.05) - imposto

print(f'Você pagará um imposto de R${imposto}. E vai receber um salário de R${salario_receber}.')

43 - Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
- o total a pagar com desconto de 10%;
- o valor de cada parcela, no parcelamento de 3x sem juros;
- a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
- a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
pagamento = input('Digite um número que represente um pagamento total(R$): ')
try:
    pagamento = float(pagamento)
except:
    print(f'Valor incorreto. Você digitou {pagamento}. Por favor use apenas números separados por ponto.')
    exit()
total_desconto = input('Digite o número em porcentagem do desconto que será aplicado sobre o pagamento total (Exemplo: 15 (15%)): ')
try:
    total_desconto = float(total_desconto)
except:
    print(f'Valor incorreto. Você digitou: {total_desconto}. Por favor use apenas números separados por ponto. Exemplo: 15.0')
    exit()
desconto = pagamento * (1 - (total_desconto / 100))
print(f'Um valor de R${pagamento}, com um desconto de {total_desconto}%. O resultado é um novo valor de R${desconto}')
parcelas = input(f'Digite a quantidade de parcelas sem juros para o pagamento: ')
try:
    parcelas = float(parcelas)
except:
    print(f'Valor incorreto. Você digitou: {parcelas}. Por favor use apenas números. Exemplo: 6.')
    exit()
try:
    parcelamento = desconto / parcelas
except:
    print(f'Opa! Você digitou {parcelas} parcelas, se o pagamento for à vista, coloque o número 1.')
    exit()
if parcelas != 1:
    comissao = desconto * 0.05
else:
    comissao = pagamento * 0.05

print(f'Pagamento sem desconto: R${pagamento}\n'
      f'Desconto: {total_desconto}%\n'
      f'Pagamento com desconto: R${desconto}\n'
      f'Parcelas: {parcelas}\n'
      f'Valor de cada parcela: R${parcelamento}\n'
      f'Comissão do vendedor: R${comissao}')

44 - Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir
para atingir seu objetivo
degrau = 15
altura = input('Qual é a altura em metros que você deseja subir? ')
try:
    altura = float(altura)
except:
    print(f'Valor incorreto. Você digitou: {altura}. Por favor use apenas números separados por ponto. Exemplo: 10.0')
    exit()
degraus = (altura * 100) / degrau
print(f'Para subir a altura de {altura} metros. Você vai precisar subir {degraus} degraus de escada.')

45 - Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela ASCII para resolver o problema.
letra = input('Digite uma letra maiúscula qualquer: ')
try:
    letra = letra.lower()
except:
    print(f'Valor incorreto. Você digitou: {letra}, use somente letras.')
    exit()
print(f'A letra minúscula do que você digitou é: {letra}.')

46 - Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:
numeros = input('Digite um número qualquer: ')
print(f'O número invertido do valor que você escolheu é: {numeros[::-1]}.')

47 - Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
numeros = input('Digite um número qualquer: ')
for caractere in numeros:
    print(caractere)

48 - Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
segundos = input('Digite um número que representa um valor em segundos: ')
try:
    segundos = float(segundos)
except:
    print(f'Valor incorreto. Você digitou: {segundos}. Por favor use apenas números separados por ponto.')
    exit()
horas = (segundos / 60) / 60
resto = horas - ((segundos / 60) // 60)
minutos = resto * 60
resto_segundos = ((segundos / 60) - (segundos // 60)) * 60
print(f'{segundos} segundos. Isso vale {int(horas)} horas, {int(minutos)} minutos e {int(resto_segundos)} segundos.')

49 - Faça um programa para ler o horário (hora, minuto e segundo) de inicio e a duração, em segundos, de uma experiência
biológica. O programa deve resultar com o novo horário (hora, minuto e segundo) do termino da mesma.
import datetime

hora = datetime.datetime.now()
print(hora)
duracao = datetime.timedelta(days=3)
termino = hora + duracao
print(f'O programa que começa a agora tem a previsão de término as: {termino}')

50 - Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.
ano_atual = 2022
idade = input('Por favor digite um número que represente a sua idade(anos): ')
try:
    idade = int(idade)
except:
    print(f'Valor incorreto. Você digitou: {idade}. Por favor use apenas números inteiros.')
    exit()
ano_nascimento = ano_atual - idade
print(f'Você nasceu no ano de {ano_nascimento}.')

51 - Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0,0)
import math
def coordenadas(a, b):
    return math.sqrt((a * a) + (b * b))
print(coordenadas(3, 4))

52 - Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu
para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada
um ganharia do prêmio com base no valor investido.
premio = 100000
ganhadores = []
for i in range(1, 4):
    investimento = input(f'Digite o {i}º valor investido para concorrer ao premio total: ')
    try:
        investimento = float(investimento)
    except:
        print(f'Valor incorreto. Você digitou {investimento}. Por favor use apenas números inteiros.')
    ganhador = investimento * 10
    ganhadores.append(ganhador)
print(f'O primeiro lugar ganhou R${ganhadores[0]}. O segundo lugar ganhou R${ganhadores[1]} e o terceiro lugar ganhou R${ganhadores[2]}.')

53 - Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como o preço do metro de tela p.
Imprima o custo para cercar este mesmo terreno com tela.
dimensoes = []
for i in range(1, 3):
    dimensao = input(f'Qual é o valor do {i}º lado do terreno, em metros: ')
    try:
        dimensao = float(dimensao)
    except:
        print(f'Valor incorreto. Você digitou: {dimensao}. Por favor use apenas números separados por ponto. Exemplo: 5.5.')
        exit()
    dimensoes.append(dimensao)
preco = input('Digite um número que representa o preço da tela por metro (R$): ')
try:
    preco = float(preco)
except:
    print(f'Valor incorreto. Você digitou: {preco}. Por favor use apenas números separados por ponto. Exemplo 25.00')
    exit()
perimetro = (dimensoes[0] * 2) + (dimensoes[1] * 2)
print(f'Os lados do terrenos são de: {dimensoes}. O preço por metro é de R${preco}. Valor para cercar o terreno: R${perimetro * preco}')

"""

