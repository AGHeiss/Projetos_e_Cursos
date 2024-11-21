"""IF ELSE ELIF
idade = 6

if idade > 6:
    print('Idade escolar')
elif idade == 6:
    print('Cadastrar criança no primeiro ano')
else:
    print('Criança fora da idade escolar')"""

"""
for in
Ainda com dúvidas -- 
nome = 'Augusto Leonardo Farias Heiss'
for valor in enumerate(nome):
    print(valor)
    
    
nome = 'Augusto Leonardo Farias Heiss'
for letra in nome:
    print(letra, end='')
    
for repetir in range (3):
    for num in range(1, 11):
        print(num * 'Augusto ')   
        
        for repetir in range (3):
    for num in range (0, 11, 2):
        print(num * 'Augusto ')
"""
"""
resposta = ''
while resposta != 'sim':
    if resposta == 'Sim':
        break
    resposta = input('Está aprendendo o loop infinito?')

while True:
    comando = input('Está gostando do curso?')
    if comando == 'sim':
        break;
    elif comando == 'Sim':
        break;
    """
""""
#Computação científica com Python - Python para todos

name = input('Enter your name:')
print('Hello', name)

hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))
pay = hours * rate
print ('Pay:', pay)"""

"""
#Segundo exercício:
try:
    hours = float(input('Enter Hours:'))
    rate = float(input('Enter Rate:'))

except:
    print('Error, please enter numeric input')
    quit();
paya = hours * rate;
if hours > 40:
    payb = (hours - 40) * (rate * 0.5);
    paya = payb + paya

print('Pay:', paya);"""
"""
#Terceiro exercício: exemplos de funções def
try:
    hours = float(input('Enter Hours:'))
    rate = float(input('Enter Rate:'))
except:
    print('Por favor digite um valor numérico.')
    quit()

def computepay(hours, rate):
    print ('In computepay', hours, rate)
    if hours > 40:
        otp = (hours - 40) * (rate * 0.5);
        reg = hours * rate;
        pay = otp + reg;
    else:
        pay = hours * rate;
    print('Pay:', pay);
computepay(hours, rate)
"""
"""
great = -1
for num in [3,100,50,23,132,27,79]:
    if num > great:
        great = num
        print('Maior número até agora')
        print(num, great)
    else:
        print('Não é o maior número')
        print(num, great)"""

"""Quarto Exercício - Write a program which repeatedly reads numbers until the user enters "done" is entered, print
out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake
using try and except and print an error message and skip to the next number.

sum = 0;
count = 0;
while True:
    value = (input('Enter a number:'));
    if value == 'done':
        break
    try:
        number = float(value)
    except:
        print('Invalid input')
        continue
    sum = sum + number;
    count = count + 1;
print('ALL DONE')
print(count, sum, sum / count)"""

"""#Quinto exercício:

str = 'X-DSPAM-Confidence: 0.8475 '
print(str.find(' '))
num = str[19:26]
print(num)
NUM = float(num)
print(NUM + 100)"""


"""Sexto exercício: Write a program to read through a file and print the contents of the file (line by line) all in 
upper case.
file = open('mbox-short.txt')
print(file)
for line in file:
    line2 = line.rstrip()
    #print('Line:', line2)
    words = line2.split()
    #print('Words:', words)
    if len(words) < 3 or words[0] != 'From':
        continue
    print('ALL DONE', words[2])"""


