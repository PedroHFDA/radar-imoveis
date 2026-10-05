import sqlite3

import config


def criar_tabelas(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS anuncios
        (id TEXT PRIMARY KEY, preco INTEGER, endereco TEXT, link TEXT, 
        primeira_vez_visto TEXT, ultima_vez_visto TEXT)
        """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS historico_precos
        (id_anuncio TEXT, preco INTEGER, data TEXT)
    """)


if __name__ == "__main__":
    con = sqlite3.connect(config.CAMINHO_BANCO)
    cur = con.cursor()
    criar_tabelas(cur)
    res = cur.execute("SELECT name FROM sqlite_master")
    res.fetchone()
