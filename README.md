SISTEMA DE GERENCIAMENTO DE MERCEARIA
Descrição
Este programa foi desenvolvido em Python para realizar o gerenciamento básico de produtos de uma mercearia. Os dados são armazenados em um arquivo CSV, permitindo cadastrar, consultar, atualizar e excluir produtos de forma simples através de um menu interativo no terminal.
Funcionalidades
•	Cadastro de produtos.
•	Listagem de todos os produtos cadastrados.
•	Busca de produtos por ID ou nome.
•	Atualização de informações dos produtos.
•	Exclusão de produtos.
•	Armazenamento permanente dos dados em arquivo CSV.
•	Validação de entradas para evitar dados inválidos.
Estrutura dos Dados
Os produtos são armazenados no arquivo "produtos.csv" com os seguintes campos:
•	id: Identificador único do produto.
•	nome: Nome do produto.
•	categoria: Categoria do produto.
•	preco: Preço unitário do produto.
•	quantidade: Quantidade disponível em estoque.
Requisitos
•	Python 3.8 ou superior.
•	Bibliotecas utilizadas: 
o	csv (biblioteca padrão do Python)
o	os (biblioteca padrão do Python)
Como Executar
1.	Certifique-se de ter o Python instalado.
2.	Abra o terminal na pasta onde está localizado o arquivo "mercearia.py".
3.	Execute o comando:
python mercearia.py
1.	O sistema criará automaticamente o arquivo "produtos.csv" caso ele não exista.
Menu Principal
1 - Cadastrar produto 2 - Listar produtos 3 - Buscar produto 4 - Atualizar produto 5 - Excluir produto 0 - Sair
Validações Implementadas
•	Não permite cadastro de produtos com ID duplicado.
•	Não permite campos obrigatórios vazios.
•	Não permite preços negativos.
•	Não permite quantidades negativas.
•	Ignora linhas inválidas encontradas no arquivo CSV.
Autores:
•	Arthur Vinicius Nunes Rodrigues
•	Gabriel Luiz Machado e Silva
•	Pedro Lima de Araujo
Objetivo do Projeto
Este projeto foi desenvolvido com fins educacionais para praticar conceitos de programação em Python, manipulação de arquivos CSV, estruturas de dados, tratamento de exceções, modularização de código e criação de sistemas CRUD (Create, Read, Update e Delete) em ambiente de terminal.

