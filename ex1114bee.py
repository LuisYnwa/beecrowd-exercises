senha = '2002'
while True:
    senha_usuario = str(input())
    if senha_usuario == senha:
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')