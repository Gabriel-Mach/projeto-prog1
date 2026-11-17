
import csv
import os

ARQUIVO = "produtos.csv"
CAMPOS = ["id", "nome", "categoria", "preco", "quantidade"]


def criar_arquivo_se_nao_existir():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
            escritor.writeheader()
        print("Arquivo 'produtos.csv' criado com sucesso!")


def carregar_produtos():
    produtos = []
    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                try:
                    produto = {
                        "id": linha["id"],
                        "nome": linha["nome"],
                        "categoria": linha["categoria"],
                        "preco": float(linha["preco"]),
                        "quantidade": int(linha["quantidade"]),
                    }
                    produtos.append(produto)
                except (ValueError, KeyError, TypeError):
                    print("Aviso: uma linha do arquivo está com problema e foi ignorada.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Ele será criado novamente.")
        criar_arquivo_se_nao_existir()
    return produtos


def salvar_produtos(produtos):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        for produto in produtos:
            escritor.writerow({
                "id": produto["id"],
                "nome": produto["nome"],
                "categoria": produto["categoria"],
                "preco": f"{produto['preco']:.2f}",
                "quantidade": produto["quantidade"],
            })

def ler_texto_obrigatorio(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            print("Erro: este campo é obrigatório. Tente novamente.")
        else:
            return texto


def ler_preco(mensagem):
    while True:
        texto = input(mensagem).strip().replace(",", ".")  # aceita 12,50
        try:
            preco = float(texto)
        except ValueError:
            print("Erro: digite um número válido. Exemplo: 12.50")
            continue

        if preco < 0:
            print("Erro: o preço não pode ser negativo.")
        elif not preco <= 100000:  # também barra valores absurdos, como "nan" e "inf"
            print("Erro: preço inválido.")
        else:
            return preco


def ler_quantidade(mensagem):
    while True:
        texto = input(mensagem).strip()
        try:
            quantidade = int(texto)
        except ValueError:
            print("Erro: digite um número inteiro. Exemplo: 10")
            continue

        if quantidade < 0:
            print("Erro: o estoque não pode ser negativo.")
        else:
            return quantidade

def buscar_por_id(produtos, id_produto):
    """Procura um produto pelo ID. Devolve o produto ou None."""
    for produto in produtos:
        if produto["id"] == id_produto:
            return produto
    return None


def mostrar_tabela(lista_produtos):
    print()
    print(f"{'ID':<8}{'Nome':<25}{'Categoria':<15}{'Preço':>12}{'Estoque':>9}")
    print("-" * 69)
    for p in lista_produtos:
        preco_formatado = f"R$ {p['preco']:.2f}"
        print(f"{p['id']:<8}{p['nome'][:24]:<25}{p['categoria'][:14]:<15}"
              f"{preco_formatado:>12}{p['quantidade']:>9}")
    print("-" * 69)


def mostrar_produto(produto):
    print()
    print(f"ID:         {produto['id']}")
    print(f"Nome:       {produto['nome']}")
    print(f"Categoria:  {produto['categoria']}")
    print(f"Preço:      R$ {produto['preco']:.2f}")
    print(f"Estoque:    {produto['quantidade']}")


def pausar():
    input("\nPressione Enter para voltar ao menu...")

def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")
    produtos = carregar_produtos()

    id_produto = ler_texto_obrigatorio("ID do produto: ")

    if buscar_por_id(produtos, id_produto) is not None:
        print(f"Erro: o ID '{id_produto}' já está em uso. Cadastro cancelado.")
        return

    nome = ler_texto_obrigatorio("Nome: ")
    categoria = ler_texto_obrigatorio("Categoria: ")
    preco = ler_preco("Preço (R$): ")
    quantidade = ler_quantidade("Quantidade em estoque: ")

    novo_produto = {
        "id": id_produto,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade,
    }

    produtos.append(novo_produto)
    salvar_produtos(produtos)
    print("\nProduto cadastrado com sucesso!")


def listar_produtos():
    print("\n--- LISTA DE PRODUTOS ---")
    produtos = carregar_produtos()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        mostrar_tabela(produtos)
        print(f"Total de produtos: {len(produtos)}")


def buscar_produto():
    print("\n--- BUSCAR PRODUTO ---")
    produtos = carregar_produtos()

    termo = ler_texto_obrigatorio("Digite o ID ou o nome do produto: ")

    encontrados = []
    for produto in produtos:
        # ID igual ao digitado OU o termo aparece dentro do nome
        if termo == produto["id"] or termo.lower() in produto["nome"].lower():
            encontrados.append(produto)

    if len(encontrados) == 0:
        print("Produto não encontrado.")
    else:
        print(f"\n{len(encontrados)} produto(s) encontrado(s):")
        mostrar_tabela(encontrados)


def atualizar_produto():
    print("\n--- ATUALIZAR PRODUTO ---")
    produtos = carregar_produtos()

    id_produto = ler_texto_obrigatorio("ID do produto que deseja atualizar: ")
    produto = buscar_por_id(produtos, id_produto)

    if produto is None:
        print("Produto não encontrado.")
        return

    while True:
        print("\nDados atuais:")
        mostrar_produto(produto)

        print("\nO que deseja alterar?")
        print("1 - Nome")
        print("2 - Categoria")
        print("3 - Preço")
        print("4 - Quantidade em estoque")
        print("0 - Voltar ao menu")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            produto["nome"] = ler_texto_obrigatorio("Novo nome: ")
        elif opcao == "2":
            produto["categoria"] = ler_texto_obrigatorio("Nova categoria: ")
        elif opcao == "3":
            produto["preco"] = ler_preco("Novo preço (R$): ")
        elif opcao == "4":
            produto["quantidade"] = ler_quantidade("Nova quantidade: ")
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
            continue

        salvar_produtos(produtos)
        print("Produto atualizado com sucesso!")


def excluir_produto():
    print("\n--- EXCLUIR PRODUTO ---")
    produtos = carregar_produtos()

    id_produto = ler_texto_obrigatorio("ID do produto que deseja excluir: ")
    produto = buscar_por_id(produtos, id_produto)

    if produto is None:
        print("Produto não encontrado.")
        return

    mostrar_produto(produto)
    confirmacao = input("\nTem certeza que deseja excluir? (s/n): ").strip().lower()

    if confirmacao == "s":
        produtos.remove(produto)
        salvar_produtos(produtos)
        print("Produto excluído com sucesso!")
    else:
        print("Exclusão cancelada.")

def mostrar_menu():
    print("\n========== MERCEARIA ==========\n")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar produto")
    print("5 - Excluir produto")
    print("0 - Sair\n")


def main():
    criar_arquivo_se_nao_existir()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto()
            pausar()
        elif opcao == "2":
            listar_produtos()
            pausar()
        elif opcao == "3":
            buscar_produto()
            pausar()
        elif opcao == "4":
            atualizar_produto()
            pausar()
        elif opcao == "5":
            excluir_produto()
            pausar()
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida! Digite um número de 0 a 5.")


if __name__ == "__main__":
    main()
