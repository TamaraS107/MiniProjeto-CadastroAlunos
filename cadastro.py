# Mini projeto: Cadastro de alunos

# Lista para guardar os nomes
alunos = []

# Função para mostrar menu
def mostrar_menu():
    print("\n=== Sistema de Cadastro de Alunos ===")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

# Função para adicionar aluno
def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    print(f"Aluno {nome} cadastrado com sucesso!")

# Função para listar alunos
def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("\nLista de alunos:")
        for i, nome in enumerate(alunos, start=1):
            print(f"{i}. {nome}")

# Programa principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
