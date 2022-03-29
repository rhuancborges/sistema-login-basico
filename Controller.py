from binascii import b2a_base64
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Model import Cadastro
import bcrypt, re
import sqlalchemy.exc as ss

def RetornaSession():
    USUARIO = 'root'
    SENHA = ''
    HOST = 'localhost'
    PORT = '3306'
    BANCO = 'sistemalogin'

    CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

    engine = create_engine(CONN)
    Session = sessionmaker(bind=engine)
    return Session()

session = RetornaSession()

def validasenha(senha):
    c = 0
    while True:
        if len(senha)<8:
            c = -1
            break
        elif not re.search('[a-z]', senha):
            c = -1
            break
        elif not re.search('[A-Z]', senha):
            c = -1 
            break
        elif not re.search('[0-9]', senha):
            c = -1
            break
        elif not re.search('[_@$]', senha):
            c = -1
            break
        elif re.search('\s', senha):
            c = -1 
            break
        else:
            c = 0
            return True
    if c==-1:
        return False

def cadastrar(name, password, em):
    try:
        pas = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())
        x = Cadastro(nome=name, senha=pas, email=em)
        session.add(x)
        session.commit()
        print('Usuário cadastrado com sucesso')
    except Exception as e:
        print(f'Erro {e}')

def login(em, s):
    x = session.query(Cadastro).filter(Cadastro.email==em).one()
    if bcrypt.checkpw(s.encode('UTF-8'), x.senha.encode('UTF-8')):
        return True, x
    else:
        z=0
        return False, z

def email_ex(email):
    try: 
        x = session.query(Cadastro).filter(Cadastro.email==email).one()
        return True
    except ss.NoResultFound:
        return False
        