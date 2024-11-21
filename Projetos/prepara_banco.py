import mysql.connector
from mysql.connector import errorcode
from projeto_01 import Territorios
from main import teste_01


print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `maps`;")

cursor.execute("CREATE DATABASE `maps`;")

cursor.execute("USE `maps`;")

# criando tabelas
TABLES = {}
TABLES['Jogos'] = ('''
      CREATE TABLE `dias` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `data` varchar(40) NOT NULL,
      `territorio` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `nome` varchar(20) NOT NULL,
      `nickname` varchar(8) NOT NULL,
      `senha` varchar(100) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')


# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
      ("Bruno Divino", "BD", "alohomora"),
      ("Camila Ferreira", "Mila", "paozinho"),
      ("Guilherme Louro", "Cake", "python_eh_vida")
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from maps.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
jogos_sql = 'INSERT INTO dias (nome, data, territorio) VALUES (%s, %s, %s)'
jogos = [
      ('Augusto', 'Puzzle', 'Atari'),
      ('Augusto', 'Hack n Slash', 'PS2'),
      ('Augusto', 'Luta', 'PS2'),
      ('Augusto', 'FPS', 'PC'),
      ('Augusto', 'Hack n Slash', 'PS2'),
      ('Augusto', 'Corrida', 'PS2'),
]
cursor.executemany(jogos_sql, jogos)

cursor.execute('select * from maps.dias')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()