import sqlite3

import config


def criar_tabelas(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS anuncios
        (id TEXT PRIMARY KEY, preco INTEGER, metragem REAL, endereco TEXT, link TEXT, 
        primeira_vez_visto TEXT, ultima_vez_visto TEXT)
        """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS historico_precos
        (id_anuncio TEXT, preco INTEGER, data TEXT)
    """)


def salvar_anuncio(cur, anuncio, agora):

    cur.execute(
        """
            SELECT id, preco FROM anuncios WHERE id = ?
        """,
        (anuncio["id"],),
    )

    existente = cur.fetchone()

    if existente is None:
        valores = (
            anuncio["id"],
            anuncio["preco"],
            anuncio["endereco"],
            anuncio["metragem"],
            anuncio["link"],
            agora,
            agora,
        )
        valores_historico = (anuncio["id"], anuncio["preco"], agora)

        cur.execute(
            """
            INSERT INTO anuncios
            (id, preco, endereco, metragem, link, primeira_vez_visto, ultima_vez_visto)
            VALUES
            (?, ?, ?, ?, ?, ?, ?)
        """,
            valores,
        )

        cur.execute(
            """
            INSERT INTO historico_precos
            (id_anuncio, preco, data)
            VALUES
            (?, ?, ?)
        """,
            valores_historico,
        )

        return "novo"

    elif existente[1] != anuncio["preco"]:
        cur.execute(
            """
            UPDATE anuncios
            SET preco = ?, ultima_vez_visto = ?
            WHERE id = ?
        """,
            (
                anuncio["preco"],
                agora,
                anuncio["id"],
            ),
        )

        cur.execute(
            """
            INSERT INTO historico_precos
            (id_anuncio, preco, data)
            VALUES
            (?, ?, ?)
        """,
            (
                anuncio["id"],
                anuncio["preco"],
                agora,
            ),
        )

        anuncio["preco_antigo"] = existente[1]
        return "mudou"

    else:
        cur.execute(
            """
            UPDATE anuncios
            SET ultima_vez_visto = ?
            WHERE id = ?
        """,
            (agora, anuncio["id"]),
        )

        return "igual"


def buscar_ultima_execucao(cur):
    cur.execute(
        """
        SELECT MAX(ultima_vez_visto) FROM anuncios
    """
    )
    resultado = cur.fetchone()
    return resultado[0]


def buscar_sumidos(cur, ultima_execucao):
    if ultima_execucao is None:
        return []

    cur.execute(
        """
        SELECT id, endereco, preco, metragem, link
        FROM anuncios WHERE ultima_vez_visto = ?
    """,
        (ultima_execucao,),
    )
    sumidos = cur.fetchall()
    return sumidos


def buscar_anuncios(cur):
    cur.execute(
        """
        SELECT id, endereco, metragem, preco, primeira_vez_visto, ultima_vez_visto, link
        FROM anuncios
    """
    )
    anuncios = cur.fetchall()
    return anuncios


if __name__ == "__main__":
    con = sqlite3.connect(config.CAMINHO_BANCO_TESTE)
    cur = con.cursor()
    criar_tabelas(cur)
    dicionario_exemplo = {
        "id": "13121972",
        "preco": 1640000,
        "metragem": 120.0,
        "endereco": "SQS 213, Bloco F",
        "link": "link Exemplo",
    }
    data_exemplo = "2026-10-06 18:08:27"
    situacao = salvar_anuncio(cur, dicionario_exemplo, data_exemplo)
    con.commit()
    print(situacao)
    print(dicionario_exemplo)
