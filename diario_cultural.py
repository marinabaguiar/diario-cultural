titulos = []

while True:
    print("1 - Adicionar título")
    print("2 - Listar títulos")
    print("3 - Remover título")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        titulo = input("Digite o título: ")
        titulos.append(titulo)
        print("Título adicionado!")
    elif opcao == "2":
        print("Títulos:")
        for titulo in titulos:
            print(f"- {titulo}")
    elif opcao == "3":
        titulo_remover = input("Digite o título que deseja remover: ")
        titulos.remove(titulo_remover)
        print("Título removido!")
    elif opcao == "4":
        print("Saindo...")
        break
