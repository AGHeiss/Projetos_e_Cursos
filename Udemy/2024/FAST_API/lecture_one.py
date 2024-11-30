import datetime
import random
from datetime import datetime, date


cost = 10
tax_percent = .25
tax = cost * tax_percent
price = cost + tax

#print(price)

username = "Codingwithroby"
first_name = "Eric"

#print(username + " " + first_name)

first_num = 10
second_num = 2
#print(first_num)
#print(second_num)

first_num = 1
#print(first_num)
#print(second_num)

first_name = "Eric"
#print(first_name)
first_name = "Melissa"
#print(first_name)

# Going to print hello world!
# print("Hello World")
#print("Hi Eric")

# This is going over
# Multiple
# Lines
"""
This is going over
multiple
lines
"""

'''
This is going over
multiple
lines
'''

"""
Assignment

Write a Python program that can do the following:

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item.
"""
wallet = 50
item = 15
tax_percent = .03
tax = item * tax_percent
price = item + tax
wallet -= price

#print(f"You have left U${wallet}")
#Or you can do it like that:
#print(f'You have left U${50 - 15 - (15 * 0.03)}')

first_name = "Eric"
#print(f"Hi {first_name}")

sentence = "Hi {} {}"
last_name = "Roby"
#print(sentence.format(first_name, last_name))

#print(f"Hi {first_name} {last_name} I hope you are learning")

#first_name = input("Enter your first name: ")
#days = input("How many days before your birthday: ")
# print(f'Hi {first_name}, only {days} days before your birthday!')

"""
String Assignment

String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.

"""
#ANSWER:
# now = datetime.now().date()
# print(now)
# birthday = input("What's your birthday? (type as dd/mm/YYYY) ")
# birthday = datetime.strptime(birthday, "%d/%m/%Y").date()
#
# days = now - birthday
# weeks = days / 7
# year = days / 365
#
# if birthday.day >= now.day:
#     dias_restantes = birthday.day - now.day
# if birthday.month >= now.month:
#     meses_restantes = birthday.month - now.month
# if birthday.day < now.day:
#     dias_restantes = 30 - (now.day - birthday.day)
# if birthday.month < now.month:
#     meses_restantes = 12 - (now.month - birthday.month)
# if meses_restantes > 0:
#     days_left = (meses_restantes * 30) + dias_restantes
#     weeks_left = days_left / 7
# if meses_restantes == 0:
#     days_left = dias_restantes
#     weeks_left = days_left / 7
#
#
# print(f'You have {days.days} of life! Or {weeks.days} weeks. Or {year.days} years')
# print(f"There's {dias_restantes} days and {meses_restantes} months until your birthday! \n"
#       f"Or there's {days_left} days left for your birthday, or aprox. {int(weeks_left)} weeks left for your birthday.")


my_list = [80, 96, 72, 100, 8]
#print(my_list)
my_list.append(1000)
#print(my_list)
my_list.insert(3, 10000)
#print(my_list)


people_list = ["Eric", "Adil", "Jeff"]
people_list[0] = 'Mel'
#print(people_list)

"""
Lists Assignment

- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
"""
#ANSWER:
# zoo = ["Cachorro", "Cat", "Chicken", "Monkey", "Lion"]
# zoo.pop(3)
# zoo.append("Elephant")
# zoo.remove("Cachorro")
# print(zoo)
# print(zoo[0:3])

"""
- Create a variable grade holding an integer between 0 - 100

- Code if, elif, else statements to print the letter grade of the number grade variable

Grades:

A = 90 - 100

B = 80 - 89

C = 70-79

D = 60 - 69

F = 0 - 59


Example:

if grade = 87 then print('B') 
"""
# for i in range(100):
#     grade = random.randint(0, 100)
#     print(grade)
#     if 90 <= grade < 100:
#         print("Grade A")
#     elif 80 <= grade <= 89:
#         print("Grade B")
#     elif 70 <= grade <= 79:
#         print("Grade C")
#     elif 60 <= grade <= 69:
#         print("Grade D")
#     else:
#         print("Grade F")

"""
Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

- Create a while loop that prints all elements of the my_list variable 3 times.

- When printing the elements, use a for loop to print the elements

- However, if the element of the for loop is equal to Monday, continue without printing

"""
# ANSWER:
# my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#
# for i in my_list:
#     for times in range(3):
#         if i == "Monday":
#             continue
#         print(i)
# RIGHT ANSWER:
# my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# i = 0
# while i < 3:
#     i += 1
#     for x in my_list:
#         if x == "Monday":
#             print("---------")
#             continue
#         print(x)

"""
Based on the dictionary:

    my_vehicle = {
        "model": "Ford",
        "make": "Explorer",
        "year": 2018,
        "mileage": 40000
    }

- Create a for loop to print all keys and values

- Create a new variable vehicle2, which is a copy of my_vehicle

- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4

- Delete the mileage key and value from vehicle2

- Print just the keys from vehicle2 
"""
# # ANSWER
# my_vehicle = {
#         "model": "Ford",
#         "make": "Explorer",
#         "year": 2018,
#         "mileage": 40000
#     }
#
# for x, y in my_vehicle.items():
#     print(x, y)
#
# vehicle2 = my_vehicle.copy()
# vehicle2['number_of_tires'] = 4
# vehicle2.pop('mileage')
#
# for x in vehicle2:
#     print(x)
"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
"""
# # ANSWER
# def personal_information(firstname, lastname, age):
#     return {
#         "firstname": firstname,
#         "lastname" : lastname,
#         "age" : age
#     }
# dict = personal_information("Maria", "Clara", "20")
# print(dict)

"""Faça um jogo de arena!"""
# ANSWER:
# class Enemy:
#     def __init__(self, enemy_type, health_points, attack_damage):
#         self.enemy_type = enemy_type
#         self.health_points = health_points
#         self.attack_damage = attack_damage
#
#     def talk(self):
#         print(f"{self.enemy_type} is going attack you.")
#
#     def attack(self):
#         print(f"{self.enemy_type} attacks you for {self.attack_damage} damage.")
#
# class Lion(Enemy):
#     def __init__(self, enemy_type, health_points, attack_damage):
#         super().__init__(enemy_type, health_points, attack_damage)
#
#     def talk(self):
#         print("Roaaaaarrr")
#
# class Gorilla(Enemy):
#     def __init__(self, enemy_type, health_points, attack_damage):
#         super().__init__(enemy_type, health_points, attack_damage)
#
#     def talk(self):
#         print("Thump Thump. Rooooooar")
#
# class Weapon():
#     def __init__(self, weapon, attack_increased):
#         self.weapon = weapon
#         self.attack_increased = attack_increased
#
# class Hero():
#     def __init__(self, health_points, attack_damage):
#         self.health_points = health_points
#         self.attack_damage = attack_damage
#         self.weapon: Weapon = None
#         self.is_weapon_equipped = False
#
#     def talk(self):
#         print("I'm not afraid of you. I will fight against you and Jehovah will give me the victory!")
#
#     def equip_weapon(self):
#         if self.weapon is not None and not self.is_weapon_equipped:
#             self.attack_damage = self.attack_damage + self.weapon.attack_increased
#             self.is_weapon_equipped = True
#             print(f"Your attack increased!")
#
#     def attack(self):
#         print(f"Hero attacks you for {self.attack_damage} damage.")
#
# def hero_battle(hero: Hero, e2: Enemy):
#     while hero.health_points > 0 and e2.health_points > 0:
#         hero.talk()
#         e2.talk()
#         hero.attack()
#         e2.health_points -= hero.attack_damage
#         e2.attack()
#         hero.health_points -= e2.attack_damage
#         print(f"Hero has {hero.health_points} health points left.\n"
#               f"{e2.enemy_type} has {e2.health_points} health points left.")
#
#     if hero.health_points > 0:
#         print("Hero wins!")
#     else:
#         print(f"{e2.enemy_type} wins!")
#
# heroi = Hero(10, 1)
# inimigo1 = Lion("Lion", 15, 5)
# inimigo2 = Gorilla("Gorilla", 15, 5)
# espada = Weapon("Sword", 15)
# heroi.weapon = espada
# heroi.equip_weapon()
#
# hero_battle(heroi, inimigo1)

