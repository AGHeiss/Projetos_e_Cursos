# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
    
    def __init__(self, palavra, tentativas=0, acertos=[]):
       self.palavra = palavra
       self.tentativas = tentativas
       self.acertos = acertos

        
    def game(self, tentativa):
        fim = []
        
        if tentativa in self.palavra:
            if tentativa not in self.acertos:
                self.acertos.append(tentativa)
            print("\nParabéns! Você acertou!!")
            print(f"\nVocê tem mais {6 - self.tentativas} tentativa(s).")
            print(board[self.tentativas])
            for i in self.palavra:
                if i in self.acertos:
                    print(i + " ", end='')
                    
                    continue
                
                print('_ ', end='')
        else:
            for i in self.palavra:
                if i in self.acertos:
                    print(i + " ", end='')
                    continue
                print('_ ', end='')
            self.tentativas += 1
            if self.tentativas == 6:
                print("\nVocê perdeu. \n O jogo começará novamente.")
                self.acertos.clear()
                self.tentativas = 0
                
            print(f"\nSinto muito, você errou! Tente novamente, você tem mais {6 - self.tentativas} tentativa(s).")
            print(board[self.tentativas])

    def game_over(self):
        letras = 0
        letraspalavra = []
        for i in self.acertos:
            if i in self.palavra:
                letras += 1
        for n in self.palavra:
            if n not in letraspalavra:
                letraspalavra.append(n)
        if letras == len(letraspalavra):
            print(f"\n Parabéns. Você ganhou o jogo! A palavra é {self.palavra}\n ")
            self.acertos.clear()
            self.tentativas = 0

                
            

	# Método Construtor

	# Método para adivinhar a letra
	
	# Método para verificar se o jogo terminou
		
	# Método para verificar se o jogador venceu
		
	# Método para não mostrar a letra no board
		
	# Método para checar o status do game e imprimir o board na tela

jogo = Hangman('leite')
jogo.game('l')
jogo.game('e')
jogo.game('i')
jogo.game('t')
jogo.game_over()
jogo.game('l')
jogo.game_over()
jogo.game('l')
jogo.game('l')
jogo.game('l')
jogo.game_over()
jogo.game('e')
jogo.game('i')
jogo.game('t')
jogo.game_over()
