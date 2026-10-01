import requests

import config

resposta = requests.get(
    f"https://www.dfimoveis.com.br/venda/df/brasilia/asa-sul/apartamento?valorfinal={config.PRECO_MAXIMO}"
)

with open(config.CAMINHO_DADOS, "w", encoding="utf-8") as f:
    f.write(resposta.text)
