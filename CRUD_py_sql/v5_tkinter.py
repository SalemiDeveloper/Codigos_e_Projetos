import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123123123",
    database="teste_db_python"
)
cursor = conexao.cursor()

# Funções para interagir com o banco de dados
def inserir():
    nome_produto = entry_nome_produto.get()
    try:
        valor = int(entry_valor.get())
        comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
        cursor.execute(comando)
        conexao.commit()
        messagebox.showinfo("Sucesso", f"Produto {nome_produto} inserido com sucesso.")
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido. Insira um número inteiro.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def listar():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    listbox_produtos.delete(0, tk.END)
    if resultado:
        for row in resultado:
            listbox_produtos.insert(tk.END, f"Nome: {row[1]}, Valor: {row[2]}")
    else:
        listbox_produtos.insert(tk.END, "Nenhum produto cadastrado.")

def atualizar():
    nome_produto = entry_nome_produto.get()
    try:
        valor = int(entry_valor.get())
        comando = f'SELECT * FROM vendas WHERE nome_produto = "{nome_produto}"'
        cursor.execute(comando)
        produto_existe = cursor.fetchone()
        if produto_existe:
            comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
            cursor.execute(comando)
            conexao.commit()
            messagebox.showinfo("Sucesso", f"Produto {nome_produto} atualizado com sucesso.")
        else:
            messagebox.showerror("Erro", f"Produto {nome_produto} não encontrado.")
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido. Insira um número inteiro.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def excluir():
    nome_produto = entry_nome_produto.get()
    confirm = messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir {nome_produto}?")
    if confirm:
        comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
        cursor.execute(comando)
        conexao.commit()
        messagebox.showinfo("Sucesso", f"Produto {nome_produto} excluído com sucesso.")
    else:
        messagebox.showinfo("Cancelado", f"Exclusão de {nome_produto} cancelada.")

# Interface gráfica
root = tk.Tk()
root.title("Gerenciador de Produtos")

# Layout
tk.Label(root, text="Nome do Produto").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Valor").grid(row=1, column=0, padx=10, pady=10)

entry_nome_produto = tk.Entry(root)
entry_nome_produto.grid(row=0, column=1, padx=10, pady=10)

entry_valor = tk.Entry(root)
entry_valor.grid(row=1, column=1, padx=10, pady=10)

btn_inserir = tk.Button(root, text="Inserir Produto", command=inserir)
btn_inserir.grid(row=2, column=0, padx=10, pady=10)

btn_listar = tk.Button(root, text="Listar Produtos", command=listar)
btn_listar.grid(row=2, column=1, padx=10, pady=10)

btn_atualizar = tk.Button(root, text="Atualizar Produto", command=atualizar)
btn_atualizar.grid(row=3, column=0, padx=10, pady=10)

btn_excluir = tk.Button(root, text="Excluir Produto", command=excluir)
btn_excluir.grid(row=3, column=1, padx=10, pady=10)

listbox_produtos = tk.Listbox(root, width=50)
listbox_produtos.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Inicia a interface gráfica
root.mainloop()

# Fechamento da conexão com o banco de dados
cursor.close()
conexao.close()
