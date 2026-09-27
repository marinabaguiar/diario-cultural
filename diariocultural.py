import json

ARQUIVO = "titulos.json"


def carregar_titulos():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_titulos():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(titulos, arquivo, ensure_ascii=False, indent=4)


titulos = carregar_titulos()


def escolher_tipo():
    while True:
        print("\nTipo:")
        print("1 - Livro")
        print("2 - Filme")
        print("3 - Série")

        opcao_tipo = input("Escolha o tipo: ")

        if opcao_tipo == "1":
            return "Livro"
        elif opcao_tipo == "2":
            return "Filme"
        elif opcao_tipo == "3":
            return "Série"
        else:
            print("Opção inválida.")


def escolher_status():
    while True:
        print("\nStatus:")
        print("1 - Quero consumir")
        print("2 - Em andamento")
        print("3 - Concluído")

        opcao_status = input("Escolha o status: ")

        if opcao_status == "1":
            return "Quero consumir"
        elif opcao_status == "2":
            return "Em andamento"
        elif opcao_status == "3":
            return "Concluído"
        else:
            print("Opção inválida.")


def escolher_nota():
    while True:
        nota = input("Digite uma nota de 0 a 10: ")

        try:
            nota = float(nota)

            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite um número válido.")


def adicionar_titulo():
    titulo = input("\nDigite o título: ")
    tipo = escolher_tipo()
    status = escolher_status()

    nota = None

    if status == "Concluído":
        nota = escolher_nota()

    obra = {
        "titulo": titulo,
        "tipo": tipo,
        "status": status,
        "nota": nota
    }

    titulos.append(obra)
    salvar_titulos()

    print("\nTítulo adicionado!")


def listar_titulos():
    print("\nTítulos:")

    if len(titulos) == 0:
        print("Nenhum título cadastrado.")
    else:
        for obra in titulos:
            if obra["nota"] is not None:
                print(
                    f"- {obra['titulo']} | "
                    f"{obra['tipo']} | "
                    f"{obra['status']} | "
                    f"Nota: {obra['nota']}"
                )
            else:
                print(
                    f"- {obra['titulo']} | "
                    f"{obra['tipo']} | "
                    f"{obra['status']}"
                )


def editar_titulo():
    titulo_editar = input("\nDigite o título que deseja editar: ")

    for obra in titulos:
        if obra["titulo"].lower() == titulo_editar.lower():

            print("\nO que deseja editar?")
            print("1 - Título")
            print("2 - Tipo")
            print("3 - Status")

            opcao_edicao = input("Escolha uma opção: ")

            if opcao_edicao == "1":
                obra["titulo"] = input("Digite o novo título: ")

            elif opcao_edicao == "2":
                obra["tipo"] = escolher_tipo()

            elif opcao_edicao == "3":
                novo_status = escolher_status()
                obra["status"] = novo_status

                if novo_status == "Concluído":
                    obra["nota"] = escolher_nota()
                else:
                    obra["nota"] = None

            else:
                print("Opção inválida.")
                return

            salvar_titulos()

            print("Título atualizado!")
            return

    print("Título não encontrado.")


def remover_titulo():
    titulo_remover = input("\nDigite o título que deseja remover: ")

    for obra in titulos:
        if obra["titulo"].lower() == titulo_remover.lower():
            titulos.remove(obra)
            salvar_titulos()

            print("Título removido!")
            return

    print("Título não encontrado.")


while True:
    print("\n1 - Adicionar título")
    print("2 - Listar títulos")
    print("3 - Editar título")
    print("4 - Remover título")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_titulo()

    elif opcao == "2":
        listar_titulos()

    elif opcao == "3":
        editar_titulo()

    elif opcao == "4":
        remover_titulo()

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")