biblioteca = {}

while True:
    print("Biblioteca")
    print("1. Adicionar livro")
    print("2. Remover livro")
    print("3. Buscar livro")
    print("4. Listar todos os livros")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        id_livro = input("Digite o ID do livro: ")
        if id_livro in biblioteca:
            print("Livro com este ID já existe")
        else:
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            biblioteca[id_livro] = {"Título": titulo, "Autor": autor}
            print("Livro adicionado")

    elif opcao == '2':
        id_livro = input("Digite o ID do livro a ser removido: ")
        if id_livro in biblioteca:
            del biblioteca[id_livro]
            print("Livro removido com sucesso")
        else:
            print("Livro não encontrado")

    elif opcao == '3':
        id_livro = input("Digite o ID do livro a ser buscado: ")
        if id_livro in biblioteca:
            livro = biblioteca[id_livro]
            print(f"Título: {livro['Título']}")
            print(f"Autor: {livro['Autor']}")
        else:
            print("Livro não encontrado")

    elif opcao == '4':
        if biblioteca:
            for id_livro, detalhes in biblioteca.items():
                print(f"ID: {id_livro}")
                print(f"  Título: {detalhes['Título']}")
                print(f"  Autor: {detalhes['Autor']}")
                print()
        else:
            print("Nenhum livro na biblioteca.")

    elif opcao == '5':
        print("Saindo...")
        break

    else:
        print("Opção inválida, Tente novamente")