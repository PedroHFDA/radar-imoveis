import config
from bs4 import BeautifulSoup

with open(config.CAMINHO_DADOS, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

anuncios = soup.find_all("article",attrs={"itemtype": "https://schema.org/RealEstateListing"})

print(len(anuncios))