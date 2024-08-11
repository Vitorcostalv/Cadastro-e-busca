# Programa de Cadastro de Projetos

# Lista para armazenar os projetos
projetos = []

def menu():
    print("\nMenu:")
    print("1. Cadastrar novo projeto")
    print("2. Listar todos os projetos")
    print("3. Buscar projeto por ID")
    print("4. Atualizar projeto")
    print("5. Remover projeto")
    print("6. Sair")

def cadastrar_projeto():
    projeto = {}
    projeto['id'] = input("Digite o ID do projeto: ")
    projeto['nome'] = input("Digite o nome do projeto: ")
    projeto['descricao'] = input("Digite a descrição do projeto: ")
    projeto['data_inicio'] = input("Digite a data de início (DD/MM/AAAA): ")
    projeto['data_fim'] = input("Digite a data de término (DD/MM/AAAA): ")
    projetos.append(projeto)
    print("Projeto cadastrado com sucesso!")

def listar_projetos():
    if projetos:
        print("\nLista de Projetos:")
        for projeto in projetos:
            print(f"ID: {projeto['id']}, Nome: {projeto['nome']}, Descrição: {projeto['descricao']}, Data de Início: {projeto['data_inicio']}, Data de Término: {projeto['data_fim']}")
    else:
        print("Nenhum projeto cadastrado.")

def buscar_projeto():
    id_projeto = input("Digite o ID do projeto que deseja buscar: ")
    for projeto in projetos:
        if projeto['id'] == id_projeto:
            print(f"ID: {projeto['id']}, Nome: {projeto['nome']}, Descrição: {projeto['descricao']}, Data de Início: {projeto['data_inicio']}, Data de Término: {projeto['data_fim']}")
            return
    print("Projeto não encontrado.")

def atualizar_projeto():
    id_projeto = input("Digite o ID do projeto que deseja atualizar: ")
    for projeto in projetos:
        if projeto['id'] == id_projeto:
            projeto['nome'] = input("Digite o novo nome do projeto: ")
            projeto['descricao'] = input("Digite a nova descrição do projeto: ")
            projeto['data_inicio'] = input("Digite a nova data de início (DD/MM/AAAA): ")
            projeto['data_fim'] = input("Digite a nova data de término (DD/MM/AAAA): ")
            print("Projeto atualizado com sucesso!")
            return
    print("Projeto não encontrado.")

def remover_projeto():
    id_projeto = input("Digite o ID do projeto que deseja remover: ")
    for projeto in projetos:
        if projeto['id'] == id_projeto:
            projetos.remove(projeto)
            print("Projeto removido com sucesso!")
            return
    print("Projeto não encontrado.")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_projeto()
        elif opcao == '2':
            listar_projetos()
        elif opcao == '3':
            buscar_projeto()
        elif opcao == '4':
            atualizar_projeto()
        elif opcao == '5':
            remover_projeto()
        elif opcao == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
