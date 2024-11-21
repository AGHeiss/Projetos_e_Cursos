"""
Modos de abertura de arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista gera FileExistsError
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo. Abrindo no modo 'a' -> append, se o arquivo não existir
será criado. Caso exista, o novo conteúdo será adicionado SEMPRE ao final do arquivo. Com o modo 'a', não controlamos o cursor.
+ -> Abre para o modo de atualização: Leitura e escrita.


https://docs.python.org/3/library/functions.html#open

"""