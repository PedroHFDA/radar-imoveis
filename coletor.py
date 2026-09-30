import requests

resposta = requests.get("https://www.dfimoveis.com.br/venda/df/brasilia/asa-sul/apartamento?valorfinal=2100000")

print(resposta.status_code)