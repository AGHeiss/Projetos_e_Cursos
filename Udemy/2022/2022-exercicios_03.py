"""
1 - Escreva um código que apresente a classe Pessoa, com atributos nome, endereço e telefone e, o método imprimir. O método
imprimir deve mostrar na tela os valores de todos os atributos.

class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def imprimir(self):
        print(f'Nome: {self.__nome} \n'
              f'Endereço: {self.__endereco}. \n'
              f'Telefone: {self.__telefone} ')

pessoa1 = Pessoa('Augusto Leonardo', 'Rua Lousiana, 95, Ferraz de Vasconcelos', '5511975337799')

pessoa1.imprimir()

2 - Baseando-se no exercício 1 adicione um método construtor que permita a definição de todos os atributos no momento da instanciação do objeto

class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def telefone(self):
        return self.__telefone

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone

    def imprimir(self):
        print(f'Nome: {self.__nome} \n'
              f'Endereço: {self.__endereco}. \n'
              f'Telefone: {self.__telefone} ')

pessoa1 = Pessoa('Augusto Leonardo', 'Rua Lousiana, 95, Ferraz de Vasconcelos', '5511975337799')

pessoa1.imprimir()

pessoa1.nome = 'Farias Heiss'
pessoa1.telefone = '5511969998236'
pessoa1.endereco = 'Rua Holywood, 195, Ferraz de Vasconcelos'

pessoa1.imprimir()

3 - Escreva um código que apresente a classe Quadrado, com atributos lado, área e perímetro e, os métodos calcularArea, calcularPerimetro
e imprimir. Os métodos calcularArea e calcularPerimetro devem efetuar seus respectivos cálculos e colocar os valores nos atributos area e
perimetro. O método imprimir deve mostrar na tela os valores de todos os atributos. Salienta-se que a área de um quadrado é obtida pela fórmula
(lado * lado) e o perímetro por (4 * lado).

class Quadrado:
    def __init__(self, lado):
        self.__lado = lado
        self.__perimetro = self.__lado * 4
        self.__area = self.__lado * self.__lado

    def imprimir(self):
        print(f'Lado do quadrado: {self.__lado}\n'
              f'Perímetro do quadrado: {self.__perimetro}\n'
              f'Área do quadrado: {self.__area}')

quadrado = Quadrado(16)

quadrado.imprimir()

4 -
"""

class Quadrado:
    def __init__(self, lado):
        self.__lado = lado
        self.__perimetro = self.__lado * 4
        self.__area = self.__lado * self.__lado

    def imprimir(self):
        print(f'Lado do quadrado: {self.__lado}\n'
              f'Perímetro do quadrado: {self.__perimetro}\n'
              f'Área do quadrado: {self.__area}')

quadrado = Quadrado(16)

quadrado.imprimir()


