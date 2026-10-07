# Modelo de Dados

## Tabela anuncios

| id | preco | metragem | endereco | link | primeira_vez_visto | ultima_vez_visto |
|----|-------|----------|----------|------|--------------------|------------------|
| Identificador de cada anúncio | Preço do anúncio | Metragem do imóvel | Endereço | Link | Primeira data de registro daquele anúncio | Última data de registro do anúncio |



## Tabela historico_precos

| id_anuncio | preco | data |
|------------|-------|------|
| id do anúncio | Preço registrado | Data de registro do preço |

- Anúncio novo grava em `anuncios` e grava o primeiro preço no histórico

- Caso o preço seja igual só atualiza `ultima_vez_visto` em `anuncios`

- Com o preço diferente, atualiza o preço em `anuncios` e grava uma linha nova no histórico