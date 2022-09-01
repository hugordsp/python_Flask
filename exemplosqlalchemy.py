
import os
os.system('cls')
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///db.sql', echo=True)

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

"""Criar uma classe Usuario"""

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(100))
    age = Column(Integer)

    def __repr__(self):
        return "<User(name={}, fullname={}, age={})>".format(self.name, self.fullname, self.age)

"""Criar o banco e instanciar um objeto"""

Base.metadata.create_all(engine)

poyatos = User(name="Henrique", fullname="Henrique Poyatos", age=42)

print(poyatos)

# Comando para inserir este objeto no banco
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
session.add(poyatos)
session.commit()

#Inserir um segundo registro
gustavo = User(name="Gustavo", fullname="Gustavo Miguel Moreno", age=22)
session.add(gustavo)
session.commit()

#inserindo vários de uma vez.
session.add_all([
    User(name="Fulano", fullname="Fulano de Tal", age=18),
    User(name="Ciclano", fullname="Ciclano de Tal", age=25)
])
session.commit()

#Consultando o registro "Fulano de Tal" no banco..
fulano = session.query(User).filter_by(fullname="Fulano de Tal").first()
print(fulano.name)
print(fulano.age)

#Alterar registro no banco
fulano.age = 22
session.add(fulano)
session.commit()

#Apagar um registro
gustavo = session.query(User).filter_by(name="Gustavo").first()
session.delete(gustavo)
session.commit()

#Consultar por ordem alfabética
for usuario in session.query(User).order_by(User.fullname):
    print(usuario.name, usuario.fullname)