import sqlite3

from openpyxl import Workbook

import banco
import config


def gerar_planilha(anuncios):
    wb = Workbook()
    ws = wb.active
    ws.title = "Anúncios"

    ws.append(
        [
            "ID",
            "Endereço",
            "Metragem",
            "Valor",
            "Primeiro Registro",
            "Último Registro",
            "Link",
        ]
    )

    for anuncio in anuncios:
        ws.append(anuncio)

    wb.save(config.CAMINHO_PLANILHA)


if __name__ == "__main__":
    con = sqlite3.connect(config.CAMINHO_BANCO)
    cur = con.cursor()
    anuncios = banco.buscar_anuncios(cur)
    gerar_planilha(anuncios)
