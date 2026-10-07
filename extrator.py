import json

from bs4 import BeautifulSoup

import config


def extrai_anuncios(html):
    soup = BeautifulSoup(html, "html.parser")

    blocos_json = soup.find_all("script", attrs={"type": "application/ld+json"})
    dados = None
    for bloco in blocos_json:
        if "ItemList" in bloco.string:
            dados = json.loads(bloco.string)
            break

    if dados is None:
        return []

    anuncios = []
    for oferta in dados["itemListElement"]:
        imovel = oferta["item"]
        id_oferta = imovel["identifier"]
        valor_imovel = int(imovel["offers"]["price"])
        endereco = imovel["address"]["streetAddress"]
        link = imovel["offers"]["url"]
        metragem = imovel["floorSize"]["value"]
        anuncio = {
            "id": id_oferta,
            "preco": valor_imovel,
            "endereco": endereco,
            "link": link,
            "metragem": metragem,
        }
        anuncios.append(anuncio)

    return anuncios


if __name__ == "__main__":
    with open(config.CAMINHO_DADOS, "r", encoding="utf-8") as f:
        html = f.read()

    pesquisa = extrai_anuncios(html)

    print(len(pesquisa))
    print(pesquisa[0])
