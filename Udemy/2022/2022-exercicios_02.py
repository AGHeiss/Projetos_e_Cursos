"""
1 - Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e altura. Crie os métodos
públicos necessários para sets e gets e também um método para imprimir os dados de uma pessoa.
class Identidade:

    pessoas = 0
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def altura(self):
        return self.__altura

    @nome.setter
    def novonome(self, novo_nome):
        self.__nome = novo_nome

    @idade.setter
    def novaidade(self, nova_idade):
        self.__idade = nova_idade

    @altura.setter
    def novaaltura(self, nova_altura):
        self.__altura = nova_altura

    def imprimir(self):
        print(f'O indivíduo chamado {self.__nome} tem {self.__idade} anos e mede {self.__altura} metros de altura.')

pessoa1 = Identidade('Augusto', '30', '1.92')
print(pessoa1)
pessoa1.imprimir()

print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.altura)
pessoa1.novonome = 'Leonardo'
pessoa1.novaidade = '31'
pessoa1.novaaltura = '2.00'
pessoa1.imprimir()


2 - Crie uma classe Agenda que pode armazenar 10 pessoas e seja capaz de realizar as seguintes operações:
 - void armazenaPessoa(String nome, int idade, float altura);
 - void removePessoa(String nome)
 - int buscaPessoa(String nome); // informa em que posição da agenda está a pessoa
 - void imprimeAgenda();// imprime os dados de todas as pessoas da agenda
 - void imprimePessoa(int index); // imprime os dados da pessoa que está na posição "i" da agenda.

"""

