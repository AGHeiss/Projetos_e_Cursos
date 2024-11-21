"""
15 - Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão é:
G = R * 180 / math.pi, sendo G o ângulo em graus e R em radianos, e pi = 3,14.
radianos = input('Escreva um valor em radianos (rad): ')
try:
    radianos = float(radianos)
except:
    print(f'Você digitou {radianos}, é necessário usar somente números separados por ponto. Exemplo: 1.0')
    exit()
angulo = radianos * 180 / math.pi
print(f'Você digitou {radianos} rad, isso equivale a {angulo} graus')

16 - Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros. A fórmula de conversão é:
C = P * 2,54 sendo C o comprimento em centímetros e P o comprimento em polegadas.
polegada = input('Informe um número que representa um comprimento em polegadas (inch): ')
try:
    polegada = float(polegada)
except:
    print(f'Você digitou {polegada}, por favor escreva somente números separados por pontos. Exemplo: 30.0')
    exit()
centimetro = polegada * 2.54
print(f'Você escreveu {polegada} inch, isso equivale a {centimetro} cm')

17 - Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas. A fórmula de conversão é:
P = C / 2,54, sendo C o comprimento em centímetros e P o comprimento em polegadas.
centimetros = input('Informe um número representando um comprimento em centímetros(cm): ')
try:
    centimetros = float(centimetros)
except:
    print(f'Você digitou {centimetros}, por favor use somente números separados por ponto. Exemplo: 100.0')
    exit()
polegada = centimetros / 2.54
print(f'Você digitou {centimetros}, esse valor equivale em polegadas a {polegada} inch')

18 - Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. A fórmula de conversão é:
L = 1000 * M, sendo L o volume em litros e M o volume em metros cúbicos
metros_volume = input('Escreva um número que representa o volume em metros cúbicos: ')
try:
    metros_volume = float(metros_volume)
except:
    print(f'Você digitou {metros_volume}, por favor use somente números separados por ponto. Exemplo: 1.0')
litros = metros_volume * 1000
print(f'Você digitou {metros_volume} m³, esse valor equivale a {litros} l')

19 - Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. A fórmula de conversão é:
M = L / 1000, sendo L o volume em litros e M o volume em metros cúbicos.
litros = input('Digite um número representando uma quantidade em litros (l): ')
try:
    litros = float(litros)
except:
    print(f'Você digitou {litros}, por favor use somente números separados por ponto. Exemplo: 1000.0')
    exit()
metros_cubicos = litros / 1000
print(f'Você digitou {litros} l, esse valor equivale a {metros_cubicos} m³.')

20 - Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula de conversão é:
L = K / 0,45, sendo K a massa em quilogramas e L a massa em libras.
quilogramas = input('Digite um número representando o peso em quilogramas (kg): ')

try:
    quilogramas = float(quilogramas)
except:
    print(f'Você digitou {quilogramas}, por favor use somente números separados por ponto. Exemplo: 1.0')
    exit()
libras = quilogramas / 0.45
print(f'Você digitou {quilogramas} kg, esse valor é equivalente a {libras} lb')

21 - Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula de conversão é:
K = L * 0,45, sendo K a massa em quilogramas e L a massa em libras.
libras = input('Digite um número representando um peso em libras (lb): ')
try:
    libras = float(libras)
except:
    print(f'Você digitou {libras}. Por favor use somente números separados por ponto. Exemplo: 5.0')
    exit()
quilograma = libras * 0.45
print(f'Você digitou {libras} lb, esse valor é equivalente a {quilograma} kg')

22 - Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula de conversão é:
M = 0,91 * J, sendo J o comprimento em jardas e M o comprimento em metros.
jardas = input('Digite um número representando uma distância em jardas (yard): ')
try:
    jardas = float(jardas)
except:
    print(f'Você digitou {jardas}. Por favor use somente números separados por ponto. Exemplo: 2.0')
    exit()
metros = 0.91 * jardas
print(f'Você digitou {jardas} yard. Esse valor é equivalente a {metros} metros')

23 - Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula de conversão é:
J = M / 0,91, sendo J o comprimento em jardas e M o comprimento em metros.
metros = input('Digite um número que representa uma distância em metros(m): ')
try:
    metros = float(metros)
except:
    print(f'Você digitou {metros}. Por favor use somente números separados por ponto.')
    exit()
jardas = metros / 0.91
print(f'Você digitou {metros} metros. Esse valor equivale a {jardas} yard.')

24 - Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. A fórmula de conversão é:
A = M * 0,000247, sendo M a área em metros quadrados e A a área em acres.
metros_quadrado = input('Digite um número que representa uma área em metros quadrados(m²): ')
try:
    metros_quadrado = float(metros_quadrado)
except:
    print(f'Você digitou {metros_quadrado}. Por favor, use somente números separados por ponto. Exemplo: 5000.0')
    exit()
acres = metros_quadrado * 0.000247
print(f'Você digitou {metros_quadrado} m². Esse valor é equivalente a {acres} acres')

25 - Leia um valor de área em acres e apresente-o convertido em metros quadrados m². A fórmula de conversão é:
M = A * 4048,58, sendo M a área em metros quadrados e A a área em acres.
acres = input('Digite um número que representa uma área em acres: ')
try:
    acres = float(acres)
except:
    print(f'Você digitou {acres}. Por favor use somente números separados por ponto. Exemplo: 1.5')
    exit()
metro_quadrado = acres * 4048.58
print(f'Você digitou {acres} acres. Esse valor é equivalente a {metro_quadrado} m²')

26 - Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares. A fórmula de conversão é:
H = M * 0,0001, sendo M a área em metros quadrados e H a área em hectares.
metro_quadrado = input('Digite um número que representa uma área em metros quadrados(m²): ')
try:
    metro_quadrado = float(metro_quadrado)
except:
    print(f'Você digitou {metro_quadrado}. Por favor, use somente números separados por ponto. Exemplo: 10000.0')
    exit()
hectare = metro_quadrado * 0.0001
print(f'Você digitou {metro_quadrado} m². Esse valor é equivalente a {hectare} ha')

27 - Leia um valor de área em hectares e apresente-o convertido em metros quadrados m². A fórmula de conversão é:
M = H * 10000, sendo M a área em metros quadrados e H a área em hectares.
hectares = input(f'Digite um número que representa uma área em hectares (ha): ')
try:
    hectares = float(hectares)
except:
    print(f'Você digitou {hectares}. Por favor use somente números separados por ponto. Exemplo: 2.5')
    exit()
metro_quadrado = hectares * 10000
print(f'Você digitou {hectares} ha. Esse valor é equivalente a {metro_quadrado} m²')
"""
import math































