# Radar de Imóveis

Ferramenta de análise e acompanhamento de valores e status de anúncios de imóveis online, auxiliando pessoas que visam acompanhar o mercado imobiliário. Mostra anúncios novos, removidos e mudança de preços.

## Status

- Em uso:
  - O radar já roda de ponta a ponta no DF Imóveis.

- Concluído: 
  - Investigação do primeiro portal
  - Banco de dados (SQLite) com histórico de preços
  - Resumo a cada execução: anúncios novos, que mudaram de preço e que sumiram
  - Planilha do Excel atualizada a cada execução
  - Executor para rodar com dois cliques

- Em desenvolvimento:
  - Formatação dos preços no resumo e na planilha

## Roteiro

- [x] Preparar o projeto: venv, git, GitHub
- [x] Investigar o site e descobrir onde estão os dados: [Investigação](NOTAS_INVESTIGACAO.md)
- [x] Primeiro programa: baixar uma página de um portal e extrair os anúncios
- [x] Percorrer todas as páginas e limpar os dados (preço como número, etc.)
- [x] Guardar tudo num banco (SQLite) e comparar com a execução anterior: o que é novo, o que sumiu, o que mudou de preço
- [x] Planilha no Excel atualizada a cada execução
- [x] Executor para rodar com dois cliques
- [ ] Adicionar outros portais e juntar anúncios repetidos
- [ ] Acabamento para portfólio: README completo, organização e testes

## Tecnologias

- Python
- SQLite 
- openpyxl
- requests
- BeautifulSoup