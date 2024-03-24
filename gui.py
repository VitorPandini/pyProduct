import tkinter as tk
from tkinter import messagebox
from db_operations import create_connection, create_table, insert_product, list_products

def main_window():
    window = tk.Tk()
    window.title("Cadastro de Produtos")

    # Criar a conexão com o banco de dados
    conn = create_connection()
    create_table(conn)

    # Função para cadastrar um novo produto
    def cadastrar_produto():
        nome = entry_nome.get()
        descricao = entry_descricao.get()
        valor = entry_valor.get()
        disponivel = "sim" if var_disponivel.get() == "sim" else "não"

        if nome and valor:
            try:
                insert_product(conn, nome, descricao, valor, disponivel)
                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
                listar_produtos()
            except Exception as e:
                print(e)
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    # Função para listar os produtos
    def listar_produtos():
        listbox_produtos.delete(0, tk.END)
        rows = list_products(conn)
        for row in rows:
            listbox_produtos.insert(tk.END, f"{row[0]} - {row[1]}")

    # Criar campos de entrada
    tk.Label(window, text="Nome do Produto").grid(row=0, column=0)
    entry_nome = tk.Entry(window)
    entry_nome.grid(row=0, column=1)

    tk.Label(window, text="Descrição do Produto").grid(row=1, column=0)
    entry_descricao = tk.Entry(window)
    entry_descricao.grid(row=1, column=1)

    tk.Label(window, text="Valor do Produto").grid(row=2, column=0)
    entry_valor = tk.Entry(window)
    entry_valor.grid(row=2, column=1)

    tk.Label(window, text="Disponível para Venda").grid(row=3, column=0)
    var_disponivel = tk.StringVar(value="sim")
    tk.Radiobutton(window, text="Sim", variable=var_disponivel, value="sim").grid(row=3, column=1)
    tk.Radiobutton(window, text="Não", variable=var_disponivel, value="não").grid(row=3, column=2)

    # Criar botão para cadastrar um novo produto
    tk.Button(window, text="Cadastrar Produto", command=cadastrar_produto).grid(row=4, column=0, columnspan=3)

    # Criar listbox para listar os produtos
    listbox_produtos = tk.Listbox(window, height=10, width=30)
    listbox_produtos.grid(row=5, column=0, columnspan=3)

    # Listar produtos ao iniciar
    listar_produtos()

    window.mainloop()

if _name_ == "_main_":
    main_window()