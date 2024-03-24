import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('produtos.db')
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        sql_create_table = """ CREATE TABLE IF NOT EXISTS produtos (
                                        id integer PRIMARY KEY,
                                        nome text NOT NULL,
                                        descricao text,
                                        valor real NOT NULL,
                                        disponivel text NOT NULL
                                    ); """
        c = conn.cursor()
        c.execute(sql_create_table)
    except sqlite3.Error as e:
        print(e)

def insert_product(conn, nome, descricao, valor, disponivel):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO produtos (nome, descricao, valor, disponivel) VALUES (?, ?, ?, ?)",
                 (nome, descricao, valor, disponivel))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def list_products(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT nome, valor FROM produtos ORDER BY valor ASC")
        rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)