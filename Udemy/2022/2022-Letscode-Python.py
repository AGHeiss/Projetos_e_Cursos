"""
Imagine que você queria imprimir "Aprovada(o)", caso o estudante tenha uma média superior ou igual a 7, e "Reprovado", caso a
média seja inferior a 7.

soma = 0
try:
    for i in range(1, 5):
        nota = float(input(f'Adicione a sua nota do {i} bimestre: '))
        soma = soma + nota


except:
    print(f'Por favor digite um número separado por ponto ao invés de virgula. Ex: 7.5 ou 9.0')

MEDIA = (soma) / 4
print(f'A sua média final, é de {MEDIA}.')
if MEDIA >= 7:
    print('Parabéns, você foi aprovado(a)')
elif MEDIA >=6:
    print('Você está de recuperação')
else:
    print('Sinto muito, você está reprovado(a)')

"""



