import os, time, Controller, re
from Controller import session
c=0
while True:
    print('-'*30)
    print('SISTEMA DE LOGIN E CADASTRO')
    print('-'*30)
    print('''OPÇÕES
    [1] Cadastro
    [2] Login
    [3] Finalizar programa''')
    print('-'*30)
    dec = int(input('Digite a opção desejada: '))
    os.system('cls') or None
    if dec==1:
        print('-'*20)
        print('CADASTRO')
        print('-'*20)
        nome = input('Digite seu nome: ')
        while True:
            r='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
            email = input('Digite seu email: ').strip()
            if len(email)==0:
                print('O campo email não pode ficar vazio')
                continue
            elif not re.search(r, email):
                print('Não é um email válido')
                continue
            elif Controller.email_ex(email):
                print('Esse email já está cadastrado')
                continue
            else:
                break

        while True:
            print('(A senha deve conter no mín. 8 caracteres, uma letra maiúscula, uma leta minúscula, um número, e um caracter especial ($,@,#,%,!))')
            senha = input('Digite sua senha: ')
            x = Controller.validasenha(senha)
            if x:
                break
            else:
                print('Digite uma senha melhor!')
                continue
        Controller.cadastrar(nome, senha, email) 
        time.sleep(0.3)
        os.system('cls') or None 
        continue     
    elif dec==2:
        while True:
            print('-'*20)
            print('LOGIN')
            print('-'*20)
            email = input('Digite seu email: ')
            senha = input('Digite sua senha: ')
            x,y = Controller.login(email, senha)
            os.system('cls') or None
            if x:
                print(f'Usuário {y.nome.capitalize()} logado')
                break
            else:
                print('Email e/ou senha incorretos')
                continue
        break    
    elif dec==3:
        os.system('cls') or None
        break
    else:
        os.system('cls') or None
        print('Tente novamente!')
        continue
print('Obrigado por usar esse mini-programa!')

