import mysql.connector
from flask import Flask
from flask_bcrypt import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

print("Todos os módulos foram importados com sucesso!")
