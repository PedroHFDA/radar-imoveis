import datetime as dt
import sqlite3
import time

import banco
import coletor
import config
import extrator
import planilha

todos_os_anuncios = []

agora = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for pagina in range(1, config.LIMITE_DE_PAGINAS + 1):
    resposta = coletor.baixar_pagina(pagina)
    if resposta.status_code == 404:
        break

    anuncios_da_pagina = extrator.extrai_anuncios(resposta.text)
    if not anuncios_da_pagina:
        break

    todos_os_anuncios.extend(anuncios_da_pagina)
    print(f"Página {pagina}: {len(anuncios_da_pagina)} anúncios")
    time.sleep(config.TEMPO_DE_PAUSA)

con = sqlite3.connect(config.CAMINHO_BANCO)
cur = con.cursor()
banco.criar_tabelas(cur)

novos = []
mudaram = []
iguais = []

ultima_execucao = banco.buscar_ultima_execucao(cur)

for anuncio in todos_os_anuncios:
    situacao = banco.salvar_anuncio(cur, anuncio, agora)
    if situacao == "novo":
        novos.append(anuncio)
    elif situacao == "mudou":
        mudaram.append(anuncio)
    else:
        iguais.append(anuncio)

sumiram = banco.buscar_sumidos(cur, ultima_execucao)

print(f"Última execução: {ultima_execucao}")
print(f"Novos: {len(novos)}")
print(f"Mudaram de preço: {len(mudaram)}")
print(f"Iguais: {len(iguais)}")
print(f"Sumiram: {len(sumiram)}")

con.commit()

lista_de_anuncios = banco.buscar_anuncios(cur)
planilha.gerar_planilha(lista_de_anuncios)

print(f"Total de anúncios: {len(todos_os_anuncios)}")
