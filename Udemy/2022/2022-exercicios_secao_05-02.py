"""
11 - Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos.
Por exemplo, ao número 251 corresponderá o valor 8(2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará
com a mensagem "Número inválido".
soma = 0
numeros: str = input('Digite um número inteiro qualquer: ')

for i in numeros:
    try:
        i = float(i)
    except:
        print(f'Número inválido.')
        exit()
    soma = i + soma

print(f'A soma dos algarismos do número digitado é de: {soma}.')

12 - Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido". Se o número for positivo, calcular o logaritmo deste número
import math
numeros = input('Digite um número inteiro: ')
try:
    numeros = int(numeros)
except:
    print(f'Valor incorreto. Você digitou: {numeros}. Por favor use apenas números inteiros.')
    exit()
if numeros >= 0:
    print(f'O log da base 10 deste número é {math.log10(numeros)}')
else:
    print(f'Número inválido. Você digitou: {numeros}')

13 - Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova tem peso 1, e a terceira prova tem peso 2.
Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.
soma = 0
for i in range(1, 4):
    notas = input(f'Digite a sua nota da {i}ª prova: ')
    try:
        notas = float(notas)
    except:
        print(f'Valor incorreto. Você digitou {notas}. Por favor use apenas números separados por ponto. Exemplo: 10.0')
    if notas >= 0:
        if notas <= 100:
            if i == 3:
                print(f'A {i}ª prova é a prova que tem mais peso!')
                soma = (notas * 2) + soma
            else:
                soma = notas + soma
        else:
            print(f'Número inválido. Você digitou {notas}. Use números entre 0 e 100.')
            exit()
    else:
        print(f'Número inválido. Você digitou {notas}. Use números entre 0 e 100.')
        exit()

print(f'A sua média é de {soma / 4}.')
media = soma / 4
if media >= 60:
    print(f'Você foi aprovado!')
else:
    print(f'Você foi reprovado.')


14 - A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratório,
a uma avaliação semestral e a um exame final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3;
Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça
todas as verificações necessárias.
soma = 0
for i in range(1, 4):
    notas = input(f'Digite o valor da sua {i}ª nota: ')
    try:
        notas = float(notas)
    except:
        print(f'Valor incorreto. Você digitou: {notas}. Por favor use apenas números separados por ponto. Ex: 7.0')
        exit()
    if notas >= 0:
        if notas <= 10:
            if i == 1:
                print('Essa é a primeira nota sobre o: Trabalho de laboratório')
                soma = (notas * 2) + soma
            elif i == 2:
                print('Essa é a segunda nota sobre a: Avaliação Semestral')
                soma = (notas * 3) + soma
            elif i == 3:
                print('Essa é a ultima nota sobre o: Exame final')
                soma = (notas * 5) + soma
        else:
            print(f'Valor inválido. Use apenas números entre 0 e 10. Você digitou: {notas}')
            exit()
    else:
        print(f'Valor inválido. Use apenas números entre 0 e 10. Você digitou: {notas}')
        exit()
media = soma / 10
if media >= 0:
    if media <= 2.9:
        print(f'Você foi reprovado. Sua média é de {media}.')
if media >= 3:
    if media <= 4.9:
        print(f'Você está de recuperação. Sua média é de {media}.')
if media >= 5:
    if media <= 10:
        print(f'Você está aprovado! Parabéns! Sua média é de {media}.')

15 - Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é,
domingo se 1, segunda-feira se 2, e assim por diante.
numero = input('Digite um número inteiro entre 1 e 7: ')
try:
    numero = int(numero)
except:
    print(f'Valor incorreto. Você digitou {numero}. Por favor use apenas números inteiros.')
    exit()
if numero == 1:
    print(f'O número {numero} é equivalente ao dia da semana: Domingo')
elif numero == 2:
    print(f'O número {numero} é equivalente ao dia da semana: Segunda-feira')
elif numero == 3:
    print(f'O número {numero} é equivalente ao dia da semana: Terça-feira')
elif numero == 4:
    print(f'O número {numero} é equivalente ao dia da semana: Quarta-feira')
elif numero == 5:
    print(f'O número {numero} é equivalente ao dia da semana: Quinta-feira')
elif numero == 6:
    print(f'O número {numero} é equivalente ao dia da semana: Sexta-feira')
elif numero == 7:
    print(f'O número {numero} é equivalente ao dia da semana: Sábado')
else:
    print('Número inválido. Por favor digite somente números inteiros entre 1 e 7')
    exit()

16 - Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este número. Isto é,
janeiro se 1, fevereiro se 2, e assim por diante.
numero = input('Digite um número inteiro entre 1 e 12: ')
try:
    numero = int(numero)
except:
    print(f'Valor incorreto. Você digitou {numero}. Por favor use apenas números inteiros.')
    exit()
if numero == 1:
    print(f'O número {numero} é equivalente ao mês: Janeiro')
elif numero == 2:
    print(f'O número {numero} é equivalente ao mês: Fevereiro')
elif numero == 3:
    print(f'O número {numero} é equivalente ao mês: Março')
elif numero == 4:
    print(f'O número {numero} é equivalente ao mês: Abril')
elif numero == 5:
    print(f'O número {numero} é equivalente ao mês: Maio')
elif numero == 6:
    print(f'O número {numero} é equivalente ao mês: Junho')
elif numero == 7:
    print(f'O número {numero} é equivalente ao mês: Julho')
elif numero == 8:
    print(f'O número {numero} é equivalente ao mês: Agosto')
elif numero == 9:
    print(f'O número {numero} é equivalente ao mês: Setembro')
elif numero == 10:
    print(f'O número {numero} é equivalente ao mês: Outubro')
elif numero == 11:
    print(f'O número {numero} é equivalente ao mês: Novembro')
elif numero == 12:
    print(f'O número {numero} é equivalente ao mês: Dezembro')
else:
    print('Número inválido. Por favor digite somente números inteiros entre 1 e 12')
    exit()

17 - Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A = ((basemaior + basemenor) * altura) / 2
- Lembre-se a base maior e a base menor devem ser números maiores que zero.
dimensoes = []
for i in range(1, 4):
    dimensao = input(f'Digite um número que represente um trapézio, respectivamente primeiro a base maior, depois a base menor, e por último a altura: ')
    try:
        dimensao = float(dimensao)
    except:
        print(f'Valor incorreto. Você digitou: {dimensao}. Por favor use apenas números separados por ponto. Exemplo: 10.0')
        exit()
    if dimensao >= 0:
        dimensoes.append(dimensao)
    else:
        print(f'Número inválido. Você digitou {dimensao}. Use apenas números positivos.')
        exit()
area = ((dimensoes[0] + dimensoes[1]) * dimensoes[2]) / 2
print(f'A área desse trapézio é de {area}')
"""
