import json

from bs4 import BeautifulSoup

import config

with open(config.CAMINHO_DADOS, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

blocos_json = soup.find_all("script", attrs={"type": "application/ld+json"})

for bloco in blocos_json:
    if "ItemList" in bloco.string:
        dados = json.loads(bloco.string)
        break

for anuncio in dados["itemListElement"]:
    imovel = anuncio["item"]
    id = imovel["identifier"]
    valor_imovel = int(imovel["offers"]["price"])
    endereco = imovel["address"]["streetAddress"]
    link = imovel["offers"]["url"]

    print(f"ID: {id} |Valor: {valor_imovel} |Endereço: {endereco} |Link: {link}")
