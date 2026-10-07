# Radar de Imóveis

Ferramenta de análise e acompanhamento de valores e status de anúncios de imóveis online, auxiliando pessoas que visam acompanhar o mercado imobiliário. Mostra anúncios novos, removidos e mudança de preços.

## Status

- Em desenvolvimento:
  - Banco de dados (SQLite)

- Concluído: 
  - Investigação do primeiro portal

## Roteiro

- [x] Preparar o projeto: venv, git, GitHub
- [x] Investigar o site e descobrir onde estão os dados: [Investigação](NOTAS_INVESTIGACAO.md)
- [x] Primeiro programa: baixar uma página de um portal e extrair os anúncios
- [x] Percorrer todas as páginas e limpar os dados (preço como número, etc.)
- [x] Guardar tudo num banco (SQLite) e comparar com a execução anterior: o que é novo, o que sumiu, o que mudou de preço
- [ ] Mandar um aviso com o resumo (e-mail ou Telegram)
- [ ] Executor para rodar com dois cliques
- [ ] Adicionar outros portais e juntar anúncios repetidos
- [ ] Acabamento para portfólio: README completo, organização e testes

## Tecnologias

- Python
- SQLite (Planejado)