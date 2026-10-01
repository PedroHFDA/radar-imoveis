# Investigação: DF Imóveis

## Resumo
Os dados vêm diretamente no HTML, não é necessário usar navegador e cada anúncio possui um ID próprio.

## Como montar a url de busca

https://www.dfimoveis.com.br/venda/df/brasilia/sudoeste/apartamento

Domínio: 
https://www.dfimoveis.com.br

Caminho: 
/venda/df/brasilia/asa-sul/apartamento

Query String: 

É tudo aquilo que vem depois do "?" presente na url

`&` Serve para somar os filtros dentro do Url

- pagina=2

- valorinicial=1500000

- valorfinal=1990000

Vêm 30 anúncios por página e o total aparece no filtro lateral "Tipos"

## Paginação

- Uma página que não existe responde com status **404**

- Condições de parada:
  - status **404** 
  - página sem anúncio
  - limite máximo de páginas

- Pausa de alguns segundos entre um pedido e outro


## Onde estão os dados na página

| Campo | Onde está no HTML | Exemplo |
|-------|-------------------|---------|
| Preço | `itemprop="price"`, atributo content | " 1.500.000" |
| Id | `data-id` e no final do link | data-id="1377780" |
| Descrição | `itemprop="description"` | SQS 207  Reformado  Andar Alto  Nascente |
| Valor m² | Valor m² R$ `class="body-large bold"` | 12.292
| Nome | `itemprop="name"` | SQS 213, ASA SUL, BRASILIA |
| Link | `itemprop="url"` | href="/imovel/apartamento-2-quartos-venda-asa-sul-brasilia-df-sqs-204-1421073" |
| Características | `div`s com a classe `rounded-pill`, sem etiqueta | `136 m²`, `3 Quartos`, `1 Suíte`, `1 Vaga` |

## Pegadinhas

- Um mesmo imovel pode estar anunciado duas vezes por corretores diferentes, resultando em Ids diferentes. Para isso uma solução seria comparar valores como metragem, quadra, bloco, valor, entre outras características

- Existem dois campos de descrição no mesmo anúncio um é `<h3>` curto e o outro é `<p>` com texto longo

- o preço vem como texto

- O link é relativo, sem o domínio

- As características não têm etiqueta e às vezes falta alguma

- Aparecem anúncios "Vendido"

- O site não filtra por quadra, então esse filtro fica no código

- há acentos codificados, como `&#178;` e `&#243;`

## Robots.txt

```
User-agent: *
Disallow: /imovel/impressao/
Disallow: /imovel/termo-de-visita/
Disallow: /favoritos/
Disallow: /visitas/
Disallow: /propostas/
Disallow: /conta/
Disallow: /filtros/
Disallow: /imoveis-vistos
Disallow: /busca/ajax/
Disallow: /imoveis-visitados/
Sitemap: https://www.dfimoveis.com.br/sitemap_index.xml
```

`/venda/` e `/imovel/` estão liberados porém, `/busca/ajax/` está proibido, portanto não será utilizado

## Dúvidas em aberto

- O que fazer caso o anúncio esteja como vendido?