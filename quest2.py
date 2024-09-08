''' um pequeno programa capaz de selecionar 3 funções onde é possivel adicionar e verificar elementos " usuarios"  em conjunção
com senhas presentes nas listas, ou encerrar o programa'''

usuarios = []
senhas = []

while True:
    print("\nescolha a operação que deseja:")
    print("1. cadastro")
    print("2. entrar no sistema")
    print("3. encerrar o programa")


    opcao = input("digite 1, 2 ou 3: ")

    if opcao == '1':
        nome = input("digite o seu nome: ")
        usuarios.append(nome)
        
        senha = input('crie sua senha: ')
        senhas.append(senha)



    elif opcao == '2':
        in_nome = input('digite seu nome: ')
        in_senha = input('digite sua senha: ')
        
        if in_nome in usuarios and in_senha in senha:
            print(True)
        
        else:
            print(False)

    elif opcao == '3':
        print("encerrando o programa.")
        break

