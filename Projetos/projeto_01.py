"""
O objetivo desse projeto é criar uma lógica para ser usada em um aplicativo, um aplicativo de designações de territórios para trabalho voluntário, 
que além de registrar as designações, mostrar os status principais do que já foi designado comparando com o dia de atual.

1 - Importar datetime

2 - Atribuir a data atual numa variável

3 - Perguntar para o usuário o dia que foi registrado a designação do território e armazenar numa variável
  - Perguntar para o usuário o território que foi trabalhado no dia já informado e armazenar numa variável

4 - Se o território já foi registrado naquele mesmo dia, informar ao usuário que já foi registrado essa designação e mostrar
o menu com os status de todos os territórios com base na data atual, por exemplo: 
- Os ultimos territórios trabalhados mostrando há quantos dias atrás eles foram trabalhados, 
mostrar todos os territórios desde os que ainda não foram trabalhados aos que foram designados recentemente.
- Quantas vezes os territórios foram trabalhados

5 - Registrar a designação num dicionário (exemplo) em que a chave seja a data, e o valor seja 1 caso o território foi trabalhado naquele dia, ou 0 por padrão,
mostrando que ele não foi trabalhado.

6 - Elaborar o sistema de comparações para exibir o menu de acordo com as ultimas designações atribuídas.

7 - Testar a lógica usando Python
"""
import datetime


class Territorios:
    
    def __init__(self):

        self.dia_atual = datetime.datetime.today().date()
        territorio_01 = {}
        territorio_02 = {}
        territorio_03 = {}
        territorio_04 = {}
        territorio_05 = {}
        territorio_06 = {}
        territorio_07 = {}
        territorio_08 = {}
        territorio_09 = {}
        territorio_10 = {}
        territorio_11 = {}
        territorio_12 = {}
        territorio_13 = {}
        territorio_14 = {}
        territorio_15 = {}
        territorio_16 = {}
        territorio_17 = {}
        self.territorio_01 = territorio_01
        self.territorio_02 = territorio_02
        self.territorio_03 = territorio_03
        self.territorio_04 = territorio_04
        self.territorio_05 = territorio_05
        self.territorio_06 = territorio_06
        self.territorio_07 = territorio_07
        self.territorio_08 = territorio_08
        self.territorio_09 = territorio_09
        self.territorio_10 = territorio_10
        self.territorio_11 = territorio_11
        self.territorio_12 = territorio_12
        self.territorio_13 = territorio_13
        self.territorio_14 = territorio_14
        self.territorio_15 = territorio_15
        self.territorio_16 = territorio_16
        self.territorio_17 = territorio_17
        self.dias_sem_trabalhar = []
        self.dias_trabalhados = []

    def designar_territorio(self, data_da_designacao, territorio_designado):
        self.data_da_designacao = datetime.datetime.strptime(data_da_designacao, "%d/%m/%Y").date()
        self.territorio_designado = territorio_designado
        if self.territorio_designado == 1:
            self.territorio_01[self.data_da_designacao] = 1
        elif self.territorio_designado == 2:
            self.territorio_02[self.data_da_designacao] = 1
        elif self.territorio_designado == 3:
            self.territorio_03[self.data_da_designacao] = 1
        elif self.territorio_designado == 4:
            self.territorio_04[self.data_da_designacao] = 1
        elif self.territorio_designado == 5:
            self.territorio_05[self.data_da_designacao] = 1
        elif self.territorio_designado == 6:
            self.territorio_06[self.data_da_designacao] = 1
        elif self.territorio_designado == 7:
            self.territorio_07[self.data_da_designacao] = 1
        elif self.territorio_designado == 8:
            self.territorio_08[self.data_da_designacao] = 1
        elif self.territorio_designado == 9:
            self.territorio_09[self.data_da_designacao] = 1
        elif self.territorio_designado == 10:
            self.territorio_10[self.data_da_designacao] = 1
        elif self.territorio_designado == 11:
            self.territorio_11[self.data_da_designacao] = 1
        elif self.territorio_designado == 12:
            self.territorio_12[self.data_da_designacao] = 1
        elif self.territorio_designado == 13:
            self.territorio_13[self.data_da_designacao] = 1
        elif self.territorio_designado == 14:
            self.territorio_14[self.data_da_designacao] = 1
        elif self.territorio_designado == 15:
            self.territorio_15[self.data_da_designacao] = 1
        elif self.territorio_designado == 16:
            self.territorio_16[self.data_da_designacao] = 1
        elif self.territorio_designado == 17:
            self.territorio_17[self.data_da_designacao] = 1
        else:
            print(f'Esse território {self.territorio_designado} não existe ou o valor está incorreto. Tente digitar valores entre 1 a 17!')

    def menu_trabalhos(self):
        dias_01 = []
        dias_02 = []
        dias_03 = []
        dias_04 = []
        dias_05 = []
        dias_06 = []
        dias_07 = []
        dias_08 = []
        dias_09 = []
        dias_10 = []
        dias_11 = []
        dias_12 = []
        dias_13 = []
        dias_14 = []
        dias_15 = []
        dias_16 = []
        dias_17 = []
        if len(self.territorio_01) > 0:
            for chave in self.territorio_01:
                dia = self.dia_atual - chave
                dias_01.append(dia)
            self.dias_trabalhados.append(len(dias_01))               
            self.dias_sem_trabalhar.append(min(dias_01))
        if len(self.territorio_02) > 0:
            for chave in self.territorio_02:
                dia = self.dia_atual - chave
                dias_02.append(dia)
            self.dias_trabalhados.append(len(dias_02))
            self.dias_sem_trabalhar.append(min(dias_02))
        if len(self.territorio_03) > 0:
            for chave in self.territorio_03:
                dia = self.dia_atual - chave
                dias_03.append(dia)
            self.dias_trabalhados.append(len(dias_03))
            self.dias_sem_trabalhar.append(min(dias_03))
        if len(self.territorio_04) > 0:
            for chave in self.territorio_04:
                dia = self.dia_atual - chave
                dias_04.append(dia)
            self.dias_trabalhados.append(len(dias_04))
            self.dias_sem_trabalhar.append(min(dias_04))
        if len(self.territorio_05) > 0:
            for chave in self.territorio_05:
                dia = self.dia_atual - chave
                dias_05.append(dia)
            self.dias_trabalhados.append(len(dias_05))
            self.dias_sem_trabalhar.append(min(dias_05))
        if len(self.territorio_06) > 0:
            for chave in self.territorio_06:
                dia = self.dia_atual - chave
                dias_06.append(dia)
            self.dias_trabalhados.append(len(dias_06))
            self.dias_sem_trabalhar.append(min(dias_06))
        if len(self.territorio_07) > 0:
            for chave in self.territorio_07:
                dia = self.dia_atual - chave
                dias_07.append(dia)
            self.dias_trabalhados.append(len(dias_07))
            self.dias_sem_trabalhar.append(min(dias_07))
        if len(self.territorio_08) > 0:
            for chave in self.territorio_08:
                dia = self.dia_atual - chave
                dias_08.append(dia)
            self.dias_trabalhados.append(len(dias_08))
            self.dias_sem_trabalhar.append(min(dias_08))
        if len(self.territorio_09) > 0:
            for chave in self.territorio_09:
                dia = self.dia_atual - chave
                dias_09.append(dia)
            self.dias_trabalhados.append(len(dias_09))
            self.dias_sem_trabalhar.append(min(dias_09))
        if len(self.territorio_10) > 0:
            for chave in self.territorio_10:
                dia = self.dia_atual - chave
                dias_10.append(dia)
            self.dias_trabalhados.append(len(dias_10))
            self.dias_sem_trabalhar.append(min(dias_10))
        if len(self.territorio_11) > 0:
            for chave in self.territorio_11:
                dia = self.dia_atual - chave
                dias_11.append(dia)
            self.dias_trabalhados.append(len(dias_11))
            self.dias_sem_trabalhar.append(min(dias_11))
        if len(self.territorio_12) > 0:
            for chave in self.territorio_12:
                dia = self.dia_atual - chave
                dias_12.append(dia)
            self.dias_trabalhados.append(len(dias_12))
            self.dias_sem_trabalhar.append(min(dias_12))
        if len(self.territorio_13) > 0:
            for chave in self.territorio_13:
                dia = self.dia_atual - chave
                dias_13.append(dia)
            self.dias_trabalhados.append(len(dias_13))
            self.dias_sem_trabalhar.append(min(dias_13))
        if len(self.territorio_14) > 0:
            for chave in self.territorio_14:
                dia = self.dia_atual - chave
                dias_14.append(dia)
            self.dias_trabalhados.append(len(dias_14))
            self.dias_sem_trabalhar.append(min(dias_14))
        if len(self.territorio_15) > 0:
            for chave in self.territorio_15:
                dia = self.dia_atual - chave
                dias_15.append(dia)
            self.dias_trabalhados.append(len(dias_15))
            self.dias_sem_trabalhar.append(min(dias_15))
        if len(self.territorio_16) > 0:
            for chave in self.territorio_16:
                dia = self.dia_atual - chave
                dias_16.append(dia)
            self.dias_trabalhados.append(len(dias_16))
            self.dias_sem_trabalhar.append(min(dias_16))
        if len(self.territorio_17) > 0:
            for chave in self.territorio_17:
                dia = self.dia_atual - chave
                dias_17.append(dia)
            self.dias_trabalhados.append(len(dias_17))
            self.dias_sem_trabalhar.append(min(dias_17))
        contagem = 1
        indice = 0
        for i in self.dias_sem_trabalhar:
            print(f'Território {contagem}: {i} sem trabalhar, esse território foi trabalhado {self.dias_trabalhados[indice]} vezes'
                  ' em todo o período registrado')
            contagem += 1
            indice += 1



      

