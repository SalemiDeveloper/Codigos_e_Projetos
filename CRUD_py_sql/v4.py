import mysql.connector
from mysql.connector import Error

# abrir o WORKBENCH -> user: root password: 123123123

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123123123",
    database="teste_db_python"
)

cursor = conexao.cursor()

# CRUD
def menu():
    menu = """\n
    ================ MENU ================
    [1] Inserir produto
    [2] Listar produtos
    [3] Atualizar produto
    [4] Excluir produto
    [5] Sair do programa
    """
    return input(menu)

def inserir():
    # CREATE
    nome_produto = input("Insira o nome do produto para por no banco de dados: ")
    valor = int(input(f"Insira o valor de {nome_produto}: "))
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados
    print(f"Produto {nome_produto} inserido com sucesso.")

def listar():
    # READ
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados
    if resultado:
        print("\nProdutos cadastrados:")
        for row in resultado:
            print(f"Nome: {row[1]}, Valor: {row[2]}")
    else:
        print("Nenhum produto cadastrado.")

def verificar_produtos():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    return cursor.fetchall()

def verificar_produto_existe(nome_produto):
    comando = f'SELECT * FROM vendas WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    return cursor.fetchone()

def atualizar():
    # Verifica se há produtos
    resultado = verificar_produtos()
    if resultado:
        nome_produto = input("Insira o nome do produto que deseja alterar no banco de dados: ")
        # Verifica se o produto existe
        produto_existe = verificar_produto_existe(nome_produto)
        if produto_existe:
            valor = int(input(f"Insira o valor do {nome_produto} a ser alterado: "))
            comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
            cursor.execute(comando)
            conexao.commit()
            print(f"Produto {nome_produto} atualizado com sucesso.")
        else:
            print(f"Operação inválida! Produto {nome_produto} não encontrado.")
    else:
        print("Operação inválida! Não há produtos para atualizar.")

def excluir():
    # Verifica se há produtos
    resultado = verificar_produtos()
    if resultado:
        nome_produto = input("Insira o nome do produto que deseja deletar no banco de dados: ")
        # Verifica se o produto existe
        produto_existe = verificar_produto_existe(nome_produto)
        if produto_existe:
            confirm = input(f"Tem certeza que deseja excluir {nome_produto}? s/n: ")
            if confirm.lower() == "s":
                comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
                cursor.execute(comando)
                conexao.commit()
                print(f"Produto {nome_produto} excluído com sucesso.")
            else:
                print(f"Exclusão de {nome_produto} cancelada.")
        else:
            print(f"Operação inválida! Produto {nome_produto} não encontrado.")
    else:
        print("Operação inválida! Não há produtos para excluir.")

def main():
    while True:
        opcao = menu()

        if opcao == "1":
            inserir()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            atualizar()
        elif opcao == "4":
            excluir()
        elif opcao == "5":
            print("Obrigado, até a próxima!")
            break
        else:
            print("\nOperação inválida. Selecione novamente.")

    cursor.close()
    conexao.close()

main()
