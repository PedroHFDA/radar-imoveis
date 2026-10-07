import requests

import config


def baixar_pagina(numero_da_pagina):
    resposta = requests.get(
        f"{config.URL_BUSCA}pagina={numero_da_pagina}"
        f"&valorfinal={config.PRECO_MAXIMO}"
        f"&vagasdegaragem={config.VAGAS_DE_GARAGEM}"
    )

    return resposta


if __name__ == "__main__":
    coleta = baixar_pagina(1)
    print(coleta.status_code)
    with open(config.CAMINHO_DADOS, "w", encoding="utf-8") as f:
        f.write(coleta.text)
