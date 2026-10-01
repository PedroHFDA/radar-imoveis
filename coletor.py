import requests

resposta = requests.get("https://www.dfimoveis.com.br/venda/df/brasilia/asa-sul/apartamento?valorfinal=1990000")

with open("dados/pagina1.html", "w", encoding="utf-8") as f:
    f.write(resposta.text)