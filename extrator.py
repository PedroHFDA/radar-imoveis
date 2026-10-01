import json

from bs4 import BeautifulSoup

import config

with open(config.CAMINHO_DADOS, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

blocos_json = soup.find_all("script", attrs={"type": "application/ld+json"})

dados = json.loads(blocos_json[1].string)
print(len(dados["itemListElement"]))
