import requests

PRECO_MAXIMO = 1990000

resposta = requests.get(f"https://www.dfimoveis.com.br/venda/df/brasilia/asa-sul/apartamento?valorfinal={PRECO_MAXIMO}")

with open("dados/pagina1.html", "w", encoding="utf-8") as f:
    f.write(resposta.text)