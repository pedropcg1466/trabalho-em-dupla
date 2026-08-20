# agenda.py

contatos = []


def cadastrar_contato():
    pass


def listar_contatos():
    pass


def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ")
    for contato in contatos:
        if contato["nome"] == nome:
            print("Contato encontrado:")
            print("Nome:", contato["nome"])
            print("Telefone:", contato["telefone"])
            print("Email:", contato["email"])
            return
    print("Contato não encontrado.")


def remover_contato():
    nome = input("Digite o nome do contato que deseja remover: ")
    for contato in contatos:
        if contato["nome"] == nome:
            contatos.remove(contato)
            print("Contato removido com sucesso.")
            return
    print("Contato não encontrado.")


while True:
    print("\n=== Agenda de Contatos ===")
    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        buscar_contato()
    elif opcao == "4":
        remover_contato()
    elif opcao == "5":
        print("Até logo!")
        break
    else:
        print("Opção inválida.")
        
