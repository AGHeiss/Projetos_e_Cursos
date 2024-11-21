"""
1. Escreva um programa que:
(a) - Crie/abra um arquivo de texto de nome "arq.txt"
(b) - Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere "0"
(c) - Feche o arquivo
Agora, abre e leia o arquivo, caractere por caractere, e escreva na tela todos os caracteres armazenados.

import os

with open('2022-arq.txt', 'a+') as file:
    while True:
        mensagem = input('Digite a sua mensagem para salvar no documento principal: ')
        file.write(mensagem)
        file.write('\n')
        if mensagem == '0':
            break

with open('2022-arq.txt', 'r+') as file:
    for line in file:
        print(line)

2. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas linhas esse arquivo possui.
lines = 0
with open('2022-arq.txt', 'r+') as file:
    linhas = file.readlines()
    print(f'Esse arquivo tem {len(linhas)} linhas')

3. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais
vogais = 0
with open('2022-arq.txt', 'r+') as file:
    for line in file:
        for word in line:
            for letter in word:
                if letter == 'a':
                    vogais = vogais + 1
                elif letter == 'e':
                    vogais = vogais + 1
                elif letter == 'i':
                    vogais = vogais + 1
                elif letter == 'o':
                    vogais = vogais + 1
                elif letter == 'u':
                    vogais = vogais + 1
                print(vogais)
                print(letter)

4. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais e quantas são consoantes.

vogais = 0
consoantes = 0
with open('2022-arq.txt', 'r+') as file:
    for line in file:
        for letra in line:
            if letra == 'a':
                vogais = vogais + 1
            elif letra == 'e':
                vogais = vogais + 1
            elif letra == 'i':
                vogais = vogais + 1
            elif letra == 'o':
                vogais = vogais + 1
            elif letra == 'u':
                vogais = vogais + 1
            else:
                consoantes = consoantes + 1


print(vogais)
print(consoantes)

5. Faça um programa que receba do usuário um arquivo texto e um caractere. Mostre na tela quantas vezes aquele caractere ocorre dentro do arquivo.

contagem = 0
with open('2022-arq.txt', 'r+') as file:
    mensagem = input('Escreva um caractere: ')
    if len(mensagem) > 1:
        print(f'Você escreveu {len(mensagem)} caracteres, favor escrever somente 1.')
    else:
        print(f'Obrigado, esse foi o caractere digitado: {mensagem}')
        for line in file:
            for letra in line:
                if letra == mensagem:
                    contagem = contagem + 1
        print (f'Esse caractere ocorre {contagem} vezes dentro do arquivo')

6. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas vezes cada letra do alfabeto aparece dentro do arquivo.
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0

with open('2022-arq.txt', 'r+') as file:
    for line in file:
        for letra in line:
            if letra == 'a':
                a = a + 1
            elif letra == 'b':
                b = b + 1
            elif letra == 'c':
                c = c + 1
            elif letra == 'd':
                d = d + 1
            elif letra == 'e':
                e = e + 1
            elif letra == 'f':
                f = f + 1
            elif letra == 'g':
                g = g + 1
            elif letra == 'h':
                h = h + 1
            elif letra == 'i':
                i = i + 1
            elif letra == 'j':
                j = j + 1
            elif letra == 'k':
                k = k + 1
            elif letra == 'l':
                l = l + 1
            elif letra == 'm':
                m = m + 1
            elif letra == 'n':
                n = n + 1
            elif letra == 'o':
                o = o + 1
            elif letra == 'p':
                p = p + 1
            elif letra == 'q':
                q = q + 1
            elif letra == 'r':
                r = r + 1
            elif letra == 's':
                s = s + 1
            elif letra == 't':
                t = t + 1
            elif letra == 'u':
                u = u + 1
            elif letra == 'v':
                v = v + 1
            elif letra == 'w':
                w = w + 1
            elif letra == 'x':
                x = x + 1
            elif letra == 'y':
                y = y + 1
            elif letra == 'z':
                z = z + 1

print(dict(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, k=k, l=l, m=m, n=n, o=o, p=p, q=q, r=r, s=s, t=t, u=u, v=v, w=w, x=x, y=y, z=z))

7 - Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto contendo o texto do arquivo de entrada, mas com as vogais substituídas por '*'.

with open('2022-arq.txt', 'r+') as file:
    with open('2022-texto3.txt', 'w+') as file2:
        for line in file:
            for letra in line:
                if letra == 'a':
                    file2.write('*')
                elif letra == 'e':
                    file2.write('*')
                elif letra == 'i':
                    file2.write('*')
                elif letra == 'o':
                    file2.write('*')
                elif letra == 'u':
                    file2.write('*')
                else:
                    file2.write(letra)

8 - Faça um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas.
Os nomes dos arquivos serão fornecidos, via teclado, pelo usuário. A função que converte maiúscula para minúscula é o toupper().
Ela é aplicada em cada caractere da string.

with open('2022-arq.txt', 'r+') as file:
    with open('2022-texto3.txt', 'w+') as file2:
        for line in file:
            for letra in line:
                letra2 = letra.upper()
                file2.write(letra2)

9 - Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com o conteúdo dos dois primeiros juntos (o conteúdo do primeiro
seguido do conteúdo do segundo).

with open('2022-arq.txt', 'r+') as file:
    with open('2022-texto3.txt', 'r+') as file2:
        with open('2022-texto4.txt', 'w+') as file3:
            for line in file:
                for letra in line:
                    file3.write(letra)
            for line2 in file2:
                for letra2 in line2:
                    file3.write(letra2)

10 - Faça um programa que receba o nome de um arquivo de entrada e outro de saída. O arquivo de entrada contém em cada linha o nome de uma
cidade (ocupando 40 caracteres) e o seu número de habitantes. O programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde
aparece o nome da cidade mais populosa seguida pelo seu número de habitantes.

MAIOR = 0
with open('2022-texto4.txt', 'r+') as file:
    for linha in file:
        h = linha[11:20]
        hab = h.strip()
        habitantes = float(hab)
        if habitantes > MAIOR:
            MAIOR = habitantes


print(MAIOR)

"""
import os











