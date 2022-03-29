from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = 'root'
SENHA = ''
HOST = 'localhost'
PORT = '3306'
BANCO = 'sistemalogin'

CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

engine = create_engine(CONN)
Session = sessionmaker(bind=engine)
session=Session()
Base=declarative_base()

class Cadastro(Base):
    __tablename__='cadastro'
    nome=Column(String(50))
    senha=Column(String(100))
    email=Column(String(50), primary_key=True)

Base.metadata.create_all(engine)
