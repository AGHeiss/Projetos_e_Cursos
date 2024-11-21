"""
1 - Faça um programa que leia um número inteiro e o imprima.
programa = input('Digite um número inteiro qualquer: ')
print(f'O número que você digitou é {int(programa)}')

2 - Faça um programa que leia um número real e o imprima
programa = input('Digite um número real qualquer: ')
print(f'O número que você digitou é {float(programa)}')

3 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
soma = 0
for n in range(1, 4):
    numero = input(f'Digite o {n}º número inteiro qualquer: ')
    soma = soma + int(numero)

print(f'A soma dos valores digitados é de {soma}')

4 - Leia um número real e imprima o resultado do quadrado desse número.
numero = input('Digite um número real qualquer: ')
numero = float(numero)
numero = numero * numero
print(f'O quadrado do número que você digitou é de {numero}')

5 - Leia um número real e imprima a quinta parte deste número
numero = input('Digite um número real qualquer: ')
numero = float(numero)
numero = numero / 5
print(f'A quinta parte do número que você digitou é igual a: {numero}')

6 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula da conversão é:
F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
celsius = input('Digite a temperatura atual (ºC): ')
celsius = float(celsius)
fahrenheit = celsius * (9.0 / 5.0) + 32.0
print(f'A temperatura em graus Celsius que você digitou equivale a {fahrenheit} graus Fahrenheit')

7 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A fórmula da conversão é:
C = 5.0 * (F - 32.0) / 9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
fahrenheit = input('Digite uma temperatura em graus Fahrenheit (ºF): ')
fahrenheit = float(fahrenheit)
celsius = 5.0 * (fahrenheit - 32.0) / 9.0
print(f'A temperatura que você digitou em graus Fahrenheit equivale a {celsius} graus Celsius')

8 - Leia uma temperatura em Kelvin e apresente-a convertida em graus Celsius. A fórmula de conversão é:
C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin
kelvin = input('Digite uma temperatura em Kelvin (K): ')
kelvin = float(kelvin)
celsius = kelvin - 273.15
print(f'A temperatura que você digitou em Kelvin equivale a {celsius} graus Celsius')

9 - Leia uma temperatura em graus Celsius e apresente-a convertida em Kelvin. A fórmula de conversão é:
K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
celsius = input('Digite uma temperatura em graus Celsius (ºC): ')
celsius = float(celsius)
kelvin = celsius + 273.15
print(f'A temperatura que você digitou em graus Celsius equivale a {kelvin} Kelvin')

10 - Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo).
A fórmula de conversão é: M = K / 3.6, sendo K a velocidade em km/h e M em m/s.
velocidade = input('Digite uma velocidade em km/h (quilômetros por hora): ')
velocidade = float(velocidade)
metros = velocidade / 3.6
print(f'A velocidade que você digitou equivale a {metros} m/s (metros por segundo)')

11 - Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora). A fórmula
de conversão é: K = M * 3.6, sendo K a velocidade em km/h e M em m/s.
metros = input('Digite uma velocidade em metros por segundo(m/s): ')
metros = float(metros)
velocidade = metros * 3.6
print(f'A velocidade que você digitou em m/s equivale a {velocidade} km/h')

12 - Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversão é: K = 1.61 * M, sendo
K a distância em quilômetros e M em milhas.
milhas = input('Digite uma distância em milhas (mi): ')
try:
    milhas = float(milhas)
except:
    print('Digite somente os números separados por ponto, exemplo: 5.5')
    exit()
quilometros = milhas * 1.61
print(f'A distância que você digitou em milhas equivale a {quilometros} km')

13 - Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de conversão é:
M = K / 1.61, sendo K a distância em quilômetros e M em milhas.
quilometros = input('Digite uma distância em quilômetros (km): ')
try:
    quilometros = float(quilometros)
except:
    print(f'Digite somente números separados por ponto, exemplo: 4.5. Isso foi o que você digitou: {quilometros}')
    exit()
milhas = quilometros / 1.61
print(f'Você digitou {quilometros} km, isso equivale a {milhas} mi.')

14 - Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é:
R = G * pi / 180, sendo G o ângulo em graus e R em radianos e pi = 3,14.
angulo = input('Digite um ângulo em graus(º): ')
try:
    angulo = float(angulo)
except:
    print(f'Você digitou {angulo}, por favor use apenas número separados por ponto. Exemplo: 180.0')
    exit()
radiano = angulo * math.pi / 180

print(f'Você digitou {angulo} graus, eles equivalem a {radiano} radianos')
"""
import math












