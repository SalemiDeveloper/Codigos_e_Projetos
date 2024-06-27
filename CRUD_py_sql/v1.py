import mysql.connector
from mysql.connector import Error

#abrir o WORKBENCH -> user: root password: 123123123

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123123123",
    database="teste_db_python"
)

cursor = conexao.cursor()

#CRUD

#CREATE
# nome_produto = input("Insira o nome do produto para por no banco de dados: ")
# valor = int(input(f"Insira o valor do {nome_produto}: "))
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit() #edita o banco de dados

#READ
# comando = 'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados

#UPDATE
# nome_produto = input("Insira o nome do produto que deseja alterar no banco de dados: ")
# valor = int(input(f"Insira o valor do {nome_produto} a ser alterado: "))
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()

#DELETE
# nome_produto = input("Insira o nome do produto que deseja deletar no banco de dados: ") 
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()


cursor.close()
conexao.close()
