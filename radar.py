import time

import coletor
import config
import extrator

todos_os_anuncios = []

for pagina in range(1, config.LIMITE_DE_PAGINAS + 1):
    resposta = coletor.baixar_pagina(pagina)
    if resposta.status_code == 404:
        break
    anuncios_da_pagina = extrator.extrai_anuncios(resposta.text)
    todos_os_anuncios.extend(anuncios_da_pagina)
    print(f"Página {pagina}: {len(anuncios_da_pagina)} anúncios")
    time.sleep(config.TEMPO_DE_PAUSA)

print(len(todos_os_anuncios))
