"""
32 - Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade. O programa deve calcular o valor
a ser pago por aquele lanche. Considere que a cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão abaixo:
==========================================
Especificação       Código      Preço (R$)
Cachorro Quente     100         1.20
Bauru Simples       101         1.30
Bauru com Ovo       102         1.50
Hamburguer          103         1.20
Cheeseburguer       104         1.70
Suco                105         2.20
Refrigerante        106         1.00
==========================================
def menu():

    print(
        '==========================================\n'
        'Especificação       Código      Preço (R$)\n'
        'Cachorro Quente     100         1.20\n'
        'Bauru Simples       101         1.30\n'
        'Bauru com Ovo       102         1.50\n'
        'Hamburguer          103         1.20\n'
        'Cheeseburguer       104         1.70\n'
        'Suco                105         2.20\n'
        'Refrigerante        106         1.00\n'
        '==========================================')
    codigo = int(input('Digite o código escolhido: '))
    quantidade = int(input(f'Qual é a quantidade que você gostaria do produto com o código {codigo}?'))
    if codigo == 100 and quantidade > 0:
        conta = 0
        conta = conta + 1.20 * quantidade
        print(f'Sua conta ficou com o preço de R${conta:.2f}')
        resposta = input('Deseja escolher outro lanche? Responda com sim ou não. \n --> ')
        if resposta.upper() == 'SIM':
            menu()
        else:
            print('Até a próxima!')
            exit()
    if codigo == 101 and quantidade > 0:
        conta = 0
        conta = conta + 1.30 * quantidade
        print(f'Sua conta ficou com o preço de R${conta:.2f}')
        resposta = input('Deseja escolher outro lanche? Responda com sim ou não. \n --> ')
        if resposta.upper() == 'SIM':
            menu()
        else:
            print('Até a próxima!')
            exit()
    if codigo == 102 and quantidade > 0:
        conta = 0
        conta = conta + 1.50 * quantidade
        print(f'Sua conta ficou com o preço de R${conta:.2f}')
        resposta = input('Deseja escolher outro lanche? Responda com sim ou não. \n --> ')
        if resposta.upper() == 'SIM':
            menu()
        else:
            print('Até a próxima!')
            exit()
    if codigo == 103 and quantidade > 0:
        conta = 0
        conta = conta + 1.20 * quantidade
        print(f'Sua conta ficou com o preço de R${conta:.2f}')
        resposta = input('Deseja escolher outro lanche? Responda com sim ou não. \n --> ')
        if resposta.upper() == 'SIM':
            menu()
        else:
            print('Até a próxima!')
            exit()
    if codigo == 104 and quantidade > 0:
        conta = 0
        conta = conta + 1.70 * quantidade
        print(f'Sua conta ficou com o preço de R${conta:.2f}')
        resposta = input('Deseja escolher outro lanche? Responda com sim ou não. \n --> ')
        if resposta.upper() == 'SIM':
            menu()
        else:
            print('Até a próxima!')
            exit()
    if codigo == 105 and quantidade > 0:
        conta = 0
        conta = conta + 2.20 * quantidade
        print(f'Sua conta ficou com o preço de R${conta:.2f}')
        resposta = input('Deseja escolher outro lanche? Responda com sim ou não. \n --> ')
        if resposta.upper() == 'SIM':
            menu()
        else:
            print('Até a próxima!')
            exit()
    if codigo == 106 and quantidade > 0:
        conta = 0
        conta = conta + 1.00 * quantidade
        print(f'Sua conta ficou com o preço de R${conta:.2f}')
        resposta = input('Deseja escolher outro lanche? Responda com sim ou não. \n --> ')
        if resposta.upper() == 'SIM':
            menu()
        else:
            print('Até a próxima!')
            exit()
menu()

33 - Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo, e escreva uma mensagem
em função do preço novo (de acordo com a segunda tabela).
produto = float(input('Digite o preço antigo do seu produto: '))
if produto < 50.00:
    produto = produto * 1.05
    print(f'O preço novo do seu produto é de R${produto:.2f}')
    if produto < 80.00:
        print('BARATO')
elif 50.00 <= produto <= 100.00:
    produto = produto * 1.10
    print(f'O preço novo do seu produto é de R${produto:.2f}')
    if produto < 80.00:
        print('BARATO')
    elif 80.00 <= produto <= 120:
        print('NORMAL')
elif produto > 100.00:
    produto = produto * 1.15
    print(f'O preço novo do seu produto é de R${produto:.2f}')
    if produto < 80.00:
        print('BARATO')
    elif 80.00 <= produto <= 120:
        print('NORMAL')
    elif 120.00 < produto <= 200:
        print('CARO')
    elif produto > 200.00:
        print('MUITO CARO')

34 - Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a tabela abaixo, quando o aluno tem mais
de 20 faltas ocorre uma redução de conceito.
nota = float(input('Digite a sua nota do bimestre: '))
faltas = int(input('Digite as suas faltas do bimestre: '))
if 9.0 <= nota <= 10.0 and faltas <= 20:
    print('Conceito A')
elif 9.0 <= nota <= 10.0 and faltas > 20:
    print('Conceito B')
elif 7.5 <= nota <= 8.9 and faltas <= 20:
    print('Conceito B')
elif 7.5 <= nota <= 8.9 and faltas > 20:
    print('Conceito C')
elif 5.0 <= nota <= 7.4 and faltas <= 20:
    print('Conceito C')
elif 5.0 <= nota <= 7.4 and faltas > 20:
    print('Conceito D')
elif 4.0 <= nota <= 4.9 and faltas <= 20:
    print('Conceito D')
elif 4.0 <= nota <= 4.9 and faltas > 20:
    print('Conceito E')
elif 0.0 <= nota <= 3.9 and faltas <= 20:
    print('Conceito E')
elif 0.0 <= nota <= 3.9 and faltas > 20:
    print('Conceito E')
else:
    print('Você digitou uma nota inválida.')

35 - Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele mês. Note
que fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.
ano = int(input('Digite um ano, exemplo: 1982 \n'
            '--> '))

if ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
    bissexto = True
elif ano % 100 == 0:
    print(f'O ano {ano} não é bissexto!')
    bissexto = False
elif ano % 4 == 0:
    print(f'O ano {ano} é bissexto!')
    bissexto = True
else:
    print(f'O ano {ano} não é bissexto!')
    bissexto = False

mes = int(input('Digite um número de algum mês de 1 a 12: '))
if 1 <= mes <= 12:
    pass
else:
    print('Mês inválido. Tente um número de 1 a 12.')
    exit()

dia = int(input('Digite um dia do mês: '))
if 1 <= dia <= 31:
    if mes == 2:
        if dia <= 28:
            pass
        elif dia == 29:
            if bissexto:
                pass
            else:
                print('Esse dia não existe')
                exit()
        else:
            print('Esse dia não existe')
            exit()
    if mes == 4:
        if dia <= 30:
            pass
        else:
            print('Dia inválido')
            exit()
    if mes == 6:
        if dia <= 30:
            pass
        else:
            print('Dia inválido')
            exit()
    if mes == 9:
        if dia <= 30:
            pass
        else:
            print('Dia inválido')
            exit()
    if mes == 11:
        if dia <= 30:
            pass
        else:
            print('Dia inválido')
            exit()
else:
    print('Dia inválido.')
    exit()
print(f'A data que você digitou é: {dia}/{mes}/{ano}')

36 - Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:
Venda mensal                                                        Comissão
Maior ou igual a R$100.000,00                                       R$700,00 + 16% das vendas
Menor que R$100.000,00 e maior ou igual a R$80.000,00               R$650,00 + 14% das vendas
Menor que R$80.000,00 e maior ou igual a R$60.000,00                R$600,00 + 14% das vendas
Menor que R$60.000,00 e maior ou igual a R$40.000,00                R$550,00 + 14% das vendas
Menor que R$40.000,00 e maior ou igual a R$20.000,00                R$500,00 + 14% das vendas
Menor que R$20.000,00                                               R$400,00 + 14% das vendas
def vendedor():
    venda = input('Digite o valor da venda: ')
    try:
        venda = float(venda)
    except:
        print(f'Valor incorreto. Você digitou: {venda}. Por favor use apenas números separados por ponto. Exemplo: 100000.00')
        exit()

    if venda >= 100000:
        comissao = 700 + (venda * 0.16)
        print(f'Você ganhou uma comissão de R${comissao:.2f} com essa venda.')
        comecar = input('Deseja calcular outro valor? Digite sim ou não: ')
        if comecar.upper() == 'SIM':
            vendedor()
        else:
            print('Até a próxima.')
            exit()
    elif 100000 > venda >= 80000:
        comissao = 650 + (venda * 0.14)
        print(f'Você ganhou uma comissão de R${comissao:.2f} com essa venda.')
        comecar = input('Deseja calcular outro valor? Digite sim ou não: ')
        if comecar.upper() == 'SIM':
            vendedor()
        else:
            print('Até a próxima.')
            exit()
    elif 80000 > venda >= 60000:
        comissao = 600 + (venda * 0.14)
        print(f'Você ganhou uma comissão de R${comissao:.2f} com essa venda.')
        comecar = input('Deseja calcular outro valor? Digite sim ou não: ')
        if comecar.upper() == 'SIM':
            vendedor()
        else:
            print('Até a próxima.')
            exit()
    elif 60000 > venda >= 40000:
        comissao = 550 + (venda * 0.14)
        print(f'Você ganhou uma comissão de R${comissao:.2f} com essa venda.')
        comecar = input('Deseja calcular outro valor? Digite sim ou não: ')
        if comecar.upper() == 'SIM':
            vendedor()
        else:
            print('Até a próxima.')
            exit()
    elif 40000 > venda >= 20000:
        comissao = 500 + (venda * 0.14)
        print(f'Você ganhou uma comissão de R${comissao:.2f} com essa venda.')
        comecar = input('Deseja calcular outro valor? Digite sim ou não: ')
        if comecar.upper() == 'SIM':
            vendedor()
        else:
            print('Até a próxima.')
            exit()
    elif venda < 20000:
        comissao = 400 + (venda * 0.14)
        print(f'Você ganhou uma comissão de R${comissao:.2f} com essa venda.')
        comecar = input('Deseja calcular outro valor? Digite sim ou não: ')
        if comecar.upper() == 'SIM':
            vendedor()
        else:
            print('Até a próxima.')
            exit()

vendedor()


"""


