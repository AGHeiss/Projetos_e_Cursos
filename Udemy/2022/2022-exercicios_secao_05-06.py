"""
37 - As tarifas de certo parque de estacionamento são as seguintes:
- 1ª e 2ª hora - R$1,00 cada
- 3ª e 4ª hora - R$1,40 cada
- 5ª hora e seguintes - R$2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 61 minutos pagará por duas horas,
que é o mesmo que pagaria se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida deste são apresentados na forma
de pares inteiros, representando horas e minutos. Por exemplo, o par 12 50 representará "dez para a uma da tarde". Pretende-se criar um programa
que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida
se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior à da partida, isso não é uma situação de erro, antes
significará que a partida ocorreu no dia seguinte ao da chegada.
def estacionamento():
    chegada = input(
        'Digite o horário de chegada no estacionamento seguindo o modelo do exemplo: 12 50 (às 12 h e 50 min)\n'
        '-- > ')
    partida = input('Digite o horário da partida seguinte o mesmo modelo do exemplo: 14 30 (14 h e 30 min)\n'
                    '-- > ')
    chegada = chegada.split(' ')
    partida = partida.split(' ')
    hora_chegada = float(chegada[0]) + (float(chegada[1]) / 60)
    hora_partida = float(partida[0]) + (float(partida[1]) / 60)

    if hora_partida >= hora_chegada:
        tempo = hora_partida - hora_chegada
    elif hora_chegada > hora_partida:
        tempo = (24 - hora_chegada) + hora_partida

    if tempo <= 2:
        preco = tempo * 1
        if preco > 1:
            preco = 2
        print(f'O valor do seu estacionamento é de R${preco:.2f}. Você permaneceu {tempo} horas.')
    elif 2 < tempo <= 4:
        preco = ((tempo - 2) * 1.40) + 2
        if 2 < tempo <= 3:
            preco = 2 + 1.40
        if 3 < tempo <= 4:
            preco = 2 + 2.80
        print(f'O valor do seu estacionamento é de R${preco:.2f}. Você permaneceu {tempo} horas.')
    elif tempo > 4:
        preco = ((tempo - 4) * 2.00) + 4.80
        if tempo % 1 != 0:
            tempo = (int(tempo))
            preco = (((tempo - 4) * 2.00) + 4.80) + 2
        print(f'O valor do seu estacionamento é de R${preco:.2f}. Você permaneceu {tempo} horas.')
    calcular = input('Deseja fazer outro cálculo do valor do tempo estacionado? Digite sim ou não.\n'
                     '-- > ')
    if calcular.upper() == 'SIM':
        estacionamento()
    else:
        print('Obrigado. Até mais.')

estacionamento()

38 - Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: Dia, mês e ano. Teste a validade
desta data para saber se esta é uma data válida. Teste se o dia fornecido é um dia válido: dia > 0, dia <= 28 para o mês de fevereiro (29 se o
ano for bissexto), dia <= 30 em abril, junho, setembro e novembro, dia 31 <= nos outros meses. Teste a validade do mês: mês > 0 e mês < 13. Teste a validade
do ano: ano <= ano atual (use uma constante definida com o valor igual a 2008). Imprimir: "data válida" ou "data inválida" no final da execução do programa.
def nascimento():
    data = input('Digite a sua data de nascimento seguindo o modelo: DD/MM/AAAA\n'
                 '-- > ')
    data = data.split('/')
    dia = int(data[0])
    mes = int(data[1])
    ano = int(data[2])
    ano_atual = 2022

    if 0 < ano <= ano_atual:
        if ano % 400 == 0:
            bissexto = True
        elif ano % 100 == 0:
            bissexto = False
        elif ano % 4 == 0:
            bissexto = True
        else:
            bissexto = False
    else:
        print('Ano inválido. Tente outra data.')
        nascimento()

    if 0 < dia <= 31:
        if 0 < mes <= 12:
            if mes == 1:
                print(f'Essa data é válida. Dia de nascimento: {dia}/{mes}/{ano}.')
            elif mes == 2:
                if dia == 29:
                    if bissexto != True:
                        print('Esse ano não é bissexto, tente outra data.')
                        nascimento()
                    else:
                        print(f'Essa data é válida. Dia de nascimento: {dia}/{mes}/{ano}.')
                elif dia <= 28:
                    print(f'Essa data é válida. Dia de nascimento: {dia}/{mes}/{ano}.')
                elif dia >= 30:
                    print('Data inválida. Tente outra data.')
                    nascimento()
            elif mes == 3:
                print(f'Essa data é válida. Dia de nascimento: {dia}/{mes}/{ano}.')
            elif mes == 4:
                if dia <= 30:
                    print(f'Essa data é válida. Dia de nascimento: {dia}/{mes}/{ano}.')
                else:
                    print('Dia inválido. Tente outra data.')
                    nascimento()
            elif mes == 5:
                print(f'Essa data é válida. Dia de nascimento: {dia}/{mes}/{ano}.')
            elif mes == 6:
                if dia <= 30:
                    print(f'Essa data é válida. Dia de nascimento: {dia}/{mes}/{ano}.')
                else:
                    print('Dia inválido. Tente outra data.')
                    nascimento()
            elif mes == 7:
                print(f'Essa data é válida. Dia de nascimento: {dia}/{mes}/{ano}.')
            elif mes == 8:
                print(f'Essa data é válida. Dia de nascimento: {dia}/{mes}/{ano}.')
            elif mes == 9:
                if dia <= 30:
                    print(f'Essa data é válida. Dia de nascimento: {dia}/{mes}/{ano}.')
                else:
                    print('Dia inválido. Tente outra data.')
                    nascimento()
            elif mes == 10:
                print(f'Essa data é válida. Dia de nascimento: {dia}/{mes}/{ano}.')
            elif mes == 11:
                if dia <= 30:
                    print(f'Essa data é válida. Dia de nascimento: {dia}/{mes}/{ano}.')
                else:
                    print('Dia inválido. Tente outra data.')
                    nascimento()
            elif mes == 12:
                print(f'Essa data é válida. Dia de nascimento: {dia}/{mes}/{ano}.')

        else:
            print('Mês inválido. Tente novamente.')
            nascimento()

    else:
        print(f'Dia inválido. Tente novamente.')
        nascimento()



nascimento()

39 - Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera o salário atual e o tempo
de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente maior do que os funcionários
com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus adicional de salário. Faça um programa
que leia:
- O valor do salário atual do funcionário:
- O tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final reajustado, ou uma mensagem
caso o funcionário não tenha direito a nenhum aumento.
==============================================================================
Salário Atual(R$)       Reajuste        Tempo de Serviço        Bônus(R$)
Até 500,00              25%             Abaixo de 1 ano         Sem bônus
Até 1000,00             20%             De 1 a 3 anos           100,00
Até 1500,00             15%             De 4 a 6 anos           200,00
Até 2000,00             10%             De 7 a 10 anos          300,00
Acima de 2000,00        Sem reajuste    Mais de 10 anos         500,00

salario = float(input('Digite o seu salário atual: '))
servico = float(input('Digite o tempo de serviço (anos completos): '))

if salario <= 500:
    reajuste = salario * 1.25
    print(f'Seu novo salário é de R${reajuste:.2f}')
elif salario <= 1000:
    reajuste = salario * 1.20
    print(f'Seu novo salário é de R${reajuste:.2f}')
elif salario <= 1500:
    reajuste = salario * 1.15
    print(f'Seu novo salário é de R${reajuste:.2f}')
elif salario <= 2000:
    reajuste = salario * 1.10
    print(f'Seu novo salário é de R${reajuste:.2f}')
elif salario > 2000:
    reajuste = salario
    print(f'Não houve aumento. Você continua com o salário de R${reajuste}')
if servico < 1:
    print(f'Você não ganhou nenhum bonus ainda pelo seu tempo de serviço na empresa.')
elif 1 <= servico <= 3:
    print('Você ganhou um bônus de R$100,00 pelo seu tempo de serviço.')
elif 4 <= servico <= 6:
    print('Você ganhou um bônus de R$200,00 pelo seu tempo de serviço.')
elif 7 <= servico <= 10:
    print('Você ganhou um bônus de R$300,00 pelo seu tempo de serviço.')
elif servico > 10:
    print('Você ganhou um bônus de R$500,00 pelo seu tempo de serviço.')

40 - O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos. A
comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o
custo ao consumidor.
========================================================================
CUSTO DE FÁBRICA(R$)        % DO DISTRIBUIDOR   % DOS IMPOSTOS
até 12.000,00                     5%              isento
entre 12.000 e 25.000             10%             15%
acima de 25.000                   15%             20%
fabrica = float(input('Digite um custo de fábrica: '))

if fabrica < 12000:
    consumidor = fabrica * 1.05
    print(f'O custo do consumidor será de R${consumidor:.2f}')
elif 12000 <= fabrica <= 25000:
    consumidor = fabrica * 1.25
    print(f'O custo do consumidor será de R${consumidor:.2f}')
elif fabrica > 25000:
    consumidor = fabrica * 1.35
    print(f'O custo do consumidor será de R${consumidor:.2f}')

41 - Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:
IMC             CLASSIFICAÇÃO
<= 18,5          Abaixo do peso
18,6 - 24,9      Saudável
25,0 - 29,9      Peso em excesso
30,0 - 34,9      Obesidade grau I
35,0 - 39,9      Obesidade grau II(severa)
>= 40            Obesidade grau III(mórbida)
peso = float(input('Digite o seu peso(kg): '))
altura = float(input('Digite a sua altura (m): '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print('Abaixo do peso.')
elif 18.6 <= imc <= 24.9:
    print('Saudável.')
elif 25.0 <= imc <= 29.9:
    print('Peso em excesso.')
elif 30.0 <= imc <= 34.9:
    print('Obesidade grau I.')
elif 35.0 <= imc <= 39.9:
    print('Obesidade grau II(severa).')
elif imc >= 40:
    print('Obesidade grau III(mórbida).')

print(f'Seu imc é de {imc:.1f}.')
"""








