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
    if not anuncios_da_pagina:
        break

    todos_os_anuncios.extend(anuncios_da_pagina)
    print(f"Página {pagina}: {len(anuncios_da_pagina)} anúncios")
    time.sleep(config.TEMPO_DE_PAUSA)

ids_unicos = set()
for anuncio in todos_os_anuncios:
    ids_unicos.add(anuncio["id"])

print(f"IDs únicos: {len(ids_unicos)}")

print(f"Total de anúncios: {len(todos_os_anuncios)}")
