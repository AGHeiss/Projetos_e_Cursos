"""
The main objective of this project is to create an app of territory, where it can appoint territory and register the date of the appointment
on a specific dictionary of that territory, later we will be using for calculate what we want based on the dates appointed that territory.
For example we can ask the application to show us all the territory and the date all of them is with no appointment yet, so we can choose better
which territory we will appoint according to the dates with no appointment yet. This is one example but we can calculate other things based on the
date of the appointment.
"""
import sqlite3
from datetime import datetime

conn = sqlite3.connect('territorios.db')
modify = conn.cursor()

modify.execute('''
CREATE TABLE IF NOT EXISTS territorios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    territorio TEXT NOT NULL,
    data TEXT NOT NULL,
    nome TEXT NOT NULL,
    UNIQUE(territorio, data)
    )''')
conn.commit()

#Função para inserir uma designação
def appoint_territory(data_str, territorio, nome):
    novo_territorio = territorio.upper()
    novo_nome = nome.upper()
    new_date = datetime.strptime(data_str, '%d/%m/%Y').strftime('%Y-%m-%d')
    modify.execute("INSERT OR IGNORE INTO territorios (territorio, data, nome) VALUES (?, ?, ?)", (novo_territorio, new_date, novo_nome))
    conn.commit()
    
#Consultar ultima data de território
def appointed_summary():
    modify.execute('''
        SELECT
            territorio, 
            MAX(data) as last_date,
            COUNT(*) as total_appointment
        FROM territorios
        GROUP BY territorio
        ''')
    calculate = modify.fetchall()
    today = datetime.now().date()
    
    for territory, last_date, total in calculate:
        dias = (today - datetime.strptime(last_date, '%Y-%m-%d').date()).days
        print(f"Território {territory}")
        print(f"   - Última designação há {dias} dias")
        print(f"   - Total de designações: {total}")
        print("-" * 30)
        
# Ver todas as designações de cada território
def get_appointed_data_territory():
        modify.execute('''
            SELECT
                territorio,
                data,
                nome
            FROM territorios
            ORDER BY territorio, data
            
            ''')
        calculate = modify.fetchall()
        current_territory = None
        for territory, data, nome in calculate:
            if current_territory != territory:
               print(f"Território: {territory}")
               current_territory = territory
            print(f"Data: {data} | Nome: {nome}")
            
# Ver todas as designações de um nome específico
def get_name_data_territory(name):
        modify.execute('''
            SELECT
                nome,
                data,
                territorio
            FROM territorios
            ORDER BY nome
        
        ''')
        calculate = modify.fetchall()
        current_name = None
        
        for nome, data, territorio in calculate:
            if name == nome:
                if current_name != name:
                    print(f"Nome: {nome}")
                    current_name = name
                print(f"Data: {data}  |  Territorio: {territorio}")
                
def remove_appointment(data_str, territorio):
        try:
            novo_territorio = territorio.upper()
            new_data = datetime.strptime(data_str, '%d/%m/%Y').strftime('%Y-%m-%d')
            modify.execute('''
            DELETE FROM territorios WHERE data = ? AND territorio = ?          
            ''', (new_data, novo_territorio))
            conn.commit()
            if modify.rowcount > 0:
                print(f"Designação foi deletada referente a Data: {data_str} e o Território: {territorio}.")
            else:
                print(f"Designação não foi encontrada, Data {data_str} ou Território {territorio} inválido.")
        except Exception as e:
            print("Erro ao remover a designação: ", e)
  
        
        
appoint_territory("01/06/2025", "1", "TESTE")
appoint_territory("02/06/2025", "1", "TESTE")
appoint_territory("01/06/2025", "2", "TESTE")
appoint_territory("03/06/2025", "3", "TESTE 2")
appoint_territory("03/06/2025", "4", "TESTE 2")
appoint_territory("03/06/2025", "5", "TESTE 2")
appointed_summary()
get_appointed_data_territory()
get_name_data_territory("TESTE")



"""
Old code

import datetime

from pydantic import BaseModel, Field


class Territory:
    def __init__(self):

        self.day_atual = datetime.datetime.today().date()
        territory_01 = {}
        territory_02 = {}
        territory_03 = {}
        territory_04 = {}
        territory_05 = {}
        territory_06 = {}
        territory_07 = {}
        territory_08 = {}
        territory_09 = {}
        territory_10 = {}
        territory_11 = {}
        territory_12 = {}
        territory_13 = {}
        territory_14 = {}
        territory_15 = {}
        territory_16 = {}
        territory_17 = {}
        self.territory_01 = territory_01
        self.territory_02 = territory_02
        self.territory_03 = territory_03
        self.territory_04 = territory_04
        self.territory_05 = territory_05
        self.territory_06 = territory_06
        self.territory_07 = territory_07
        self.territory_08 = territory_08
        self.territory_09 = territory_09
        self.territory_10 = territory_10
        self.territory_11 = territory_11
        self.territory_12 = territory_12
        self.territory_13 = territory_13
        self.territory_14 = territory_14
        self.territory_15 = territory_15
        self.territory_16 = territory_16
        self.territory_17 = territory_17
        self.days_not_worked = []
        self.days_worked = []

    def delete_territory(self, date_of_appointment, worked_territory):
        self.date_of_appointment = datetime.datetime.strptime(date_of_appointment, "%d/%m/%Y").date()
        self.worked_territory = worked_territory
        if self.worked_territory == 1:
            keys = list(self.territory_01.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_01.pop(i)
        elif self.worked_territory == 2:
            keys = list(self.territory_02.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_02.pop(i)
        elif self.worked_territory == 3:
            keys = list(self.territory_03.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_03.pop(i)
        elif self.worked_territory == 4:
            keys = list(self.territory_04.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_04.pop(i)
        elif self.worked_territory == 5:
            keys = list(self.territory_05.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_05.pop(i)
        elif self.worked_territory == 6:
            keys = list(self.territory_06.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_06.pop(i)
        elif self.worked_territory == 7:
            keys = list(self.territory_07.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_07.pop(i)
        elif self.worked_territory == 8:
            keys = list(self.territory_08.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_08.pop(i)
        elif self.worked_territory == 9:
            keys = list(self.territory_09.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_09.pop(i)
        elif self.worked_territory == 10:
            keys = list(self.territory_10.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_10.pop(i)
        elif self.worked_territory == 11:
            keys = list(self.territory_11.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_11.pop(i)
        elif self.worked_territory == 12:
            keys = list(self.territory_12.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_12.pop(i)
        elif self.worked_territory == 13:
            keys = list(self.territory_13.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_13.pop(i)
        elif self.worked_territory == 14:
            keys = list(self.territory_14.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_14.pop(i)
        elif self.worked_territory == 15:
            keys = list(self.territory_15.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_15.pop(i)
        elif self.worked_territory == 16:
            keys = list(self.territory_16.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_16.pop(i)
        elif self.worked_territory == 17:
            keys = list(self.territory_17.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_17.pop(i)
        else:
            return f"Você digitou um território ou uma data incorreta!"

    def update_territory(self, date_of_appointment, new_date_of_appointment, worked_territory):
        self.date_of_appointment = datetime.datetime.strptime(date_of_appointment, "%d/%m/%Y").date()
        self.worked_territory = worked_territory
        self.new_date_of_appointment = datetime.datetime.strptime(new_date_of_appointment, "%d/%m/%Y").date()
        if self.worked_territory == 1:
            keys = list(self.territory_01.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_01[self.new_date_of_appointment] = 1
                    self.territory_01.pop(i)
        elif self.worked_territory == 2:
            keys = list(self.territory_02.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_02[self.new_date_of_appointment] = 1
                    self.territory_02.pop(i)
        elif self.worked_territory == 3:
            keys = list(self.territory_03.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_03[self.new_date_of_appointment] = 1
                    self.territory_03.pop(i)
        elif self.worked_territory == 4:
            keys = list(self.territory_04.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_04[self.new_date_of_appointment] = 1
                    self.territory_04.pop(i)
        elif self.worked_territory == 5:
            keys = list(self.territory_05.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_05[self.new_date_of_appointment] = 1
                    self.territory_05.pop(i)
        elif self.worked_territory == 6:
            keys = list(self.territory_06.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_06[self.new_date_of_appointment] = 1
                    self.territory_06.pop(i)
        elif self.worked_territory == 7:
            keys = list(self.territory_07.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_07[self.new_date_of_appointment] = 1
                    self.territory_07.pop(i)
        elif self.worked_territory == 8:
            keys = list(self.territory_08.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_08[self.new_date_of_appointment] = 1
                    self.territory_08.pop(i)
        elif self.worked_territory == 9:
            keys = list(self.territory_09.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_09[self.new_date_of_appointment] = 1
                    self.territory_09.pop(i)
        elif self.worked_territory == 10:
            keys = list(self.territory_10.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_10[self.new_date_of_appointment] = 1
                    self.territory_10.pop(i)
        elif self.worked_territory == 11:
            keys = list(self.territory_11.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_11[self.new_date_of_appointment] = 1
                    self.territory_11.pop(i)
        elif self.worked_territory == 12:
            keys = list(self.territory_12.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_12[self.new_date_of_appointment] = 1
                    self.territory_12.pop(i)
        elif self.worked_territory == 13:
            keys = list(self.territory_13.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_13[self.new_date_of_appointment] = 1
                    self.territory_13.pop(i)
        elif self.worked_territory == 14:
            keys = list(self.territory_14.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_14[self.new_date_of_appointment] = 1
                    self.territory_14.pop(i)
        elif self.worked_territory == 15:
            keys = list(self.territory_15.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_15[self.new_date_of_appointment] = 1
                    self.territory_15.pop(i)
        elif self.worked_territory == 16:
            keys = list(self.territory_16.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_16[self.new_date_of_appointment] = 1
                    self.territory_16.pop(i)
        elif self.worked_territory == 17:
            keys = list(self.territory_17.keys())
            for i in keys:
                if i == self.date_of_appointment:
                    self.territory_17[self.new_date_of_appointment] = 1
                    self.territory_17.pop(i)
        else:
            return f"Você digitou um território ou uma data incorreta!"

    def appoint_territory(self, date_of_appointment, worked_territory):
        self.date_of_appointment = datetime.datetime.strptime(date_of_appointment, "%d/%m/%Y").date()
        self.worked_territory = worked_territory
        if self.worked_territory == 1:
            self.territory_01[self.date_of_appointment] = 1
        elif self.worked_territory == 2:
            self.territory_02[self.date_of_appointment] = 1
        elif self.worked_territory == 3:
            self.territory_03[self.date_of_appointment] = 1
        elif self.worked_territory == 4:
            self.territory_04[self.date_of_appointment] = 1
        elif self.worked_territory == 5:
            self.territory_05[self.date_of_appointment] = 1
        elif self.worked_territory == 6:
            self.territory_06[self.date_of_appointment] = 1
        elif self.worked_territory == 7:
            self.territory_07[self.date_of_appointment] = 1
        elif self.worked_territory == 8:
            self.territory_08[self.date_of_appointment] = 1
        elif self.worked_territory == 9:
            self.territory_09[self.date_of_appointment] = 1
        elif self.worked_territory == 10:
            self.territory_10[self.date_of_appointment] = 1
        elif self.worked_territory == 11:
            self.territory_11[self.date_of_appointment] = 1
        elif self.worked_territory == 12:
            self.territory_12[self.date_of_appointment] = 1
        elif self.worked_territory == 13:
            self.territory_13[self.date_of_appointment] = 1
        elif self.worked_territory == 14:
            self.territory_14[self.date_of_appointment] = 1
        elif self.worked_territory == 15:
            self.territory_15[self.date_of_appointment] = 1
        elif self.worked_territory == 16:
            self.territory_16[self.date_of_appointment] = 1
        elif self.worked_territory == 17:
            self.territory_17[self.date_of_appointment] = 1
        else:
            print(f'This territory you typed {self.worked_territory} does not exist or it is incorrect. Please type values between 1 and 17!')

    def menu_worked_days(self):
        days_01 = []
        days_02 = []
        days_03 = []
        days_04 = []
        days_05 = []
        days_06 = []
        days_07 = []
        days_08 = []
        days_09 = []
        days_10 = []
        days_11 = []
        days_12 = []
        days_13 = []
        days_14 = []
        days_15 = []
        days_16 = []
        days_17 = []
        if len(self.territory_01) > 0:
            for key in self.territory_01:
                day = self.day_atual - key
                days_01.append(day)
            self.days_worked.append(len(days_01))               
            self.days_not_worked.append(min(days_01))
        if len(self.territory_02) > 0:
            for key in self.territory_02:
                day = self.day_atual - key
                days_02.append(day)
            self.days_worked.append(len(days_02))
            self.days_not_worked.append(min(days_02))
        if len(self.territory_03) > 0:
            for key in self.territory_03:
                day = self.day_atual - key
                days_03.append(day)
            self.days_worked.append(len(days_03))
            self.days_not_worked.append(min(days_03))
        if len(self.territory_04) > 0:
            for key in self.territory_04:
                day = self.day_atual - key
                days_04.append(day)
            self.days_worked.append(len(days_04))
            self.days_not_worked.append(min(days_04))
        if len(self.territory_05) > 0:
            for key in self.territory_05:
                day = self.day_atual - key
                days_05.append(day)
            self.days_worked.append(len(days_05))
            self.days_not_worked.append(min(days_05))
        if len(self.territory_06) > 0:
            for key in self.territory_06:
                day = self.day_atual - key
                days_06.append(day)
            self.days_worked.append(len(days_06))
            self.days_not_worked.append(min(days_06))
        if len(self.territory_07) > 0:
            for key in self.territory_07:
                day = self.day_atual - key
                days_07.append(day)
            self.days_worked.append(len(days_07))
            self.days_not_worked.append(min(days_07))
        if len(self.territory_08) > 0:
            for key in self.territory_08:
                day = self.day_atual - key
                days_08.append(day)
            self.days_worked.append(len(days_08))
            self.days_not_worked.append(min(days_08))
        if len(self.territory_09) > 0:
            for key in self.territory_09:
                day = self.day_atual - key
                days_09.append(day)
            self.days_worked.append(len(days_09))
            self.days_not_worked.append(min(days_09))
        if len(self.territory_10) > 0:
            for key in self.territory_10:
                day = self.day_atual - key
                days_10.append(day)
            self.days_worked.append(len(days_10))
            self.days_not_worked.append(min(days_10))
        if len(self.territory_11) > 0:
            for key in self.territory_11:
                day = self.day_atual - key
                days_11.append(day)
            self.days_worked.append(len(days_11))
            self.days_not_worked.append(min(days_11))
        if len(self.territory_12) > 0:
            for key in self.territory_12:
                day = self.day_atual - key
                days_12.append(day)
            self.days_worked.append(len(days_12))
            self.days_not_worked.append(min(days_12))
        if len(self.territory_13) > 0:
            for key in self.territory_13:
                day = self.day_atual - key
                days_13.append(day)
            self.days_worked.append(len(days_13))
            self.days_not_worked.append(min(days_13))
        if len(self.territory_14) > 0:
            for key in self.territory_14:
                day = self.day_atual - key
                days_14.append(day)
            self.days_worked.append(len(days_14))
            self.days_not_worked.append(min(days_14))
        if len(self.territory_15) > 0:
            for key in self.territory_15:
                day = self.day_atual - key
                days_15.append(day)
            self.days_worked.append(len(days_15))
            self.days_not_worked.append(min(days_15))
        if len(self.territory_16) > 0:
            for key in self.territory_16:
                day = self.day_atual - key
                days_16.append(day)
            self.days_worked.append(len(days_16))
            self.days_not_worked.append(min(days_16))
        if len(self.territory_17) > 0:
            for key in self.territory_17:
                day = self.day_atual - key
                days_17.append(day)
            self.days_worked.append(len(days_17))
            self.days_not_worked.append(min(days_17))
        count = 1
        index = 0
        list_api = []
        dict_api = {}
        for i in self.days_not_worked:
            list_01 = f'Territory {count}: {i} days with no appointment, this territory was appointed {self.days_worked[index]} times'
            list_api.append(list_01)
            count += 1
            index += 1
        for a in list_api:
            print(a)
        for b, c in enumerate(list_api):
            dict_api[b] = c
        return dict_api

class AppointmentRequest(BaseModel):
    date: str = Field(..., example="29/11/2024")
    territory: int = Field(..., example=1)

class AppointmentUpdate(BaseModel):
    date: str = Field(..., example="29/11/2024")
    new_date: str = Field(..., example="29/11/2024")
    territory: int = Field(..., example=1)

"""