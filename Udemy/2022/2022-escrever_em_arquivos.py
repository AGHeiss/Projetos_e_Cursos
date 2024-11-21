"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado, caso ele já exista,
o anterior será apagado e um novo será criado. Dessa forma, todo o conteúdo no arquivo anterior é perdido.


# Exemplo de escrita

with open('2022-texto2.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivos é muito fácil. \n')
    arquivo.write('Podemos colocar quantas linhas quisermos \n')
    arquivo.write('Esta é a última linha')

    with open('2022-texto3.txt', 'w') as arquivo:
    while True:
        fruta = input('Escreva uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break


"""
