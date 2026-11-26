import os
import csv

ARQUIVO = "produtos.csv"
CAMPOS = ['id', 'nome', 'preço', 'quantidade']

def criarArquivo():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(CAMPOS)

def salvarProdutos(produtos):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor =  csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        for produto in produtos:
             escritor.writerow({
                "id": produto["id"],
                "nome": produto["nome"],
                "preço":  produto['preço'],
                "quantidade": produto["quantidade"],
            })
def carregarTabela():
    produtos = []
    try:
        with open(ARQUIVO, "r", newline="", encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                produtos.append(linha)

    except FileNotFoundError:
        print("Estoque vazio")
    return produtos

def buscarID(produtos, id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            return produto
    return None

def validarTexto(mensagem): #vai evitar que o usuário deixe de preencher algo
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            print("Esse campo é obrigatório. Tente novamente.")
        else:
            return texto

def validarPreco(mensagem): #Validar o Preço
    while True:
        numero = input(mensagem).strip().replace(",",".")
        try:
            numero = float(numero)
        except ValueError:
            print("Digite um número válido! Ex: 12,50")
            continue

        if numero < 0:
            print("O número não pode ser negativo")
        else:
            return numero

def validarQuantidade(mensagem): #Validar quantidade
    while True:
        numero = input(mensagem)
        try:
            numero = int(numero)
        except ValueError:
            print("Insira uma quantidade válida")
            continue
        if numero < 0:
            print("O número não pode ser negativo")
        else:
            return numero
    
def cadastrarProduto():

    criarArquivo()  #caso não exista, vai criar
    estoque = carregarTabela()#a gente vai precisar fazer uma verificação se o ID já existe, então a gente usa isso aqui pra pode pesquisar
    id_produto = validarTexto("Id: ")

    buscarPorId = buscarID(estoque, id_produto)
    if buscarPorId is not None:
        print("Produto já cadastrado!")
        return
    
    nome = validarTexto("Nome: ")
    preco = validarPreco("Preço: ")

    quantidade = validarQuantidade("Quantidade: ")

    produto = {
        'id': id_produto,
        'nome': nome,
        'preço': preco,
        'quantidade': quantidade
    }
    with open(ARQUIVO, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames= CAMPOS)
        escritor.writerow(produto)
    print("\nProduto cadastrado com sucesso!\n")

        
def listarEstoque():
    criarArquivo()
    with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        print("=========================")
        print("LISTA DE ITENS NO ESTOQUE")
        for linha in leitor:
            print("=================")
            mostrar_produto(linha)
            print("=================")

def mostrar_produto(produto): #Mostrar um produto específico
    print(f"ID:         {produto['id']}")
    print(f"Nome:       {produto['nome']}")
    print(f"Preço:      R$ {produto['preço']}")
    print(f"Quantidade:  {produto['quantidade']}")

def atualizarProduto():
    produtos = carregarTabela()

    id_produto = validarTexto("Insira o id do produto que você deseja atualizar: ")
    produto = buscarID(produtos, id_produto)

    if produto is None:
        print("Produto não encontrado!")
        return
    while True:
        print("\nDados atuais:")
        mostrar_produto(produto)

        print("O que deseja alterar?")
        print('1) Nome \n2) Preço \n3) Quantidade \nOu S para sair')
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produto['nome'] = validarTexto('Novo nome: ')
        elif opcao == "2":
            produto['preço'] = validarPreco('Novo preço: ')
        elif opcao == "3":
            produto['quantidade'] = validarQuantidade('Nova Quantidade: ')
        elif opcao == "S":
            break
        else:
            print("Opção inválida")
        salvarProdutos(produtos)
    print("Produto atualizado com sucesso!")



def removerProduto():
    produtos = carregarTabela()

    
    id_produto = validarTexto("Insira o id do produto que você deseja excluir: ")
    produto = buscarID(produtos, id_produto)

    if produto is None:
        print("Produto não encontrado!")
        return

    mostrar_produto(produto)
    confirmar = input("\nTem certeza que deseja excluir? (s/n): ").strip().lower()
    if confirmar == 's':
        produtos.remove(produto)
        salvarProdutos(produtos)
        print("Produto excluído com sucesso!")
    else:  
        print("Opereção cancelada!")

def pausar():
    input("Pressiona Enter para voltar ao menu...")

def menu():
    print("\n========== MERCEARIA ==========\n")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Excluir produto")
    print("0 - Sair\n")


def main():
    criarArquivo()

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()
        match(opcao):
            case "1":
                cadastrarProduto()
                pausar()
            case "2":
                listarEstoque()
                pausar()
            case "3":
                atualizarProduto()
                pausar()
            case "4":
                removerProduto()
                pausar()
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção Inválida!")

if __name__ == "__main__":
    main()